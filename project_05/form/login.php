<?php
require_once('db.php');
session_start();

$login = $_POST['login'] ?? '';
$pass = $_POST['pass'] ?? '';

// Проверка на пустые поля
if (empty($login) || empty($pass)) {
    echo "Заполните все поля";
    exit;
}

// Подготовленный запрос (защита от SQL-инъекций)
$stmt = $conn->prepare("SELECT id, login, pass FROM users WHERE login = ?");
$stmt->bind_param("s", $login);
$stmt->execute();
$result = $stmt->get_result();

// Проверка наличия пользователя
if ($result->num_rows === 0) {
    echo "Неверное имя пользователя или пароль";
    exit;
}

$user = $result->fetch_assoc();

// Сравнение хеша пароля
if (!password_verify($pass, $user['pass'])) {
    echo "Неверное имя пользователя или пароль";
    exit;
}

// Успешный вход
$_SESSION['user_id'] = $user['id'];
$_SESSION['username'] = $user['login'];

echo "Добро пожаловать, " . htmlspecialchars($user['login']);

$stmt->close();
$conn->close();