<?php
/* Receives the "Start your project" form, emails it, and keeps a copy in leads.csv.
   Upload the whole site folder to Hostinger; this file works with PHP's mail() out of the box.
   Change $TO if leads should go to another inbox. */
header('Content-Type: application/json; charset=utf-8');
$TO   = 'info@xtechverse.com';
$FROM = 'website@xtechverse.com';

if ($_SERVER['REQUEST_METHOD'] !== 'POST') { http_response_code(405); echo json_encode(['ok' => false]); exit; }

$in = json_decode(file_get_contents('php://input'), true);
if (!is_array($in)) { $in = $_POST; }
if (!empty($in['hp'])) { echo json_encode(['ok' => true]); exit; }            // bot trap

$clean = fn($k, $max = 300) => trim(mb_substr(strip_tags((string)($in[$k] ?? '')), 0, $max));
$lead = [
  'time'    => date('Y-m-d H:i'),
  'name'    => $clean('name', 120),
  'phone'   => $clean('phone', 40),
  'email'   => $clean('email', 160),
  'type'    => $clean('type', 80),
  'budget'  => $clean('budget', 80),
  'details' => $clean('details', 3000),
  'page'    => $clean('page', 200),
  'lang'    => $clean('lang', 5),
  'ip'      => $_SERVER['REMOTE_ADDR'] ?? '',
];
if ($lead['name'] === '' || $lead['phone'] === '') { http_response_code(422); echo json_encode(['ok' => false]); exit; }

/* simple rate limit: one request per IP every 30 seconds */
$tmp = sys_get_temp_dir() . '/xtv_' . md5($lead['ip']);
if (is_file($tmp) && time() - filemtime($tmp) < 30) { http_response_code(429); echo json_encode(['ok' => false]); exit; }
touch($tmp);

/* keep a copy (this folder is closed to the public by .htaccess) */
$dir = __DIR__ . '/data';
if (!is_dir($dir)) { mkdir($dir, 0750, true); }
$fp = fopen($dir . '/leads.csv', 'a');
if ($fp) { fputcsv($fp, array_values($lead)); fclose($fp); }

$body = "طلب مشروع جديد من الموقع\n\n"
      . "الاسم: {$lead['name']}\nالموبايل: {$lead['phone']}\nالإيميل: {$lead['email']}\n"
      . "نوع المشروع: {$lead['type']}\nالميزانية: {$lead['budget']}\n\nالتفاصيل:\n{$lead['details']}\n\n"
      . "الصفحة: {$lead['page']}\nالوقت: {$lead['time']}\n"
      . "واتساب: https://wa.me/" . preg_replace('/\D+/', '', $lead['phone']) . "\n";
$headers = "From: X TechVerse <{$FROM}>\r\nContent-Type: text/plain; charset=UTF-8\r\n";
if (filter_var($lead['email'], FILTER_VALIDATE_EMAIL)) { $headers .= "Reply-To: {$lead['email']}\r\n"; }
$sent = @mail($TO, '=?UTF-8?B?' . base64_encode('طلب جديد: ' . $lead['name']) . '?=', $body, $headers);

echo json_encode(['ok' => true, 'mailed' => (bool)$sent]);
