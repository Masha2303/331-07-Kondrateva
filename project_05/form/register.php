<?php
require_once('db.php');

$login = $_POST['login'];
$pass = $_POST['pass'];
$repeatpass = $_POST['repeatpass'];
$email = $_POST['email'];

// Проверка на пустые поля
if (empty($login)  empty($pass)  empty($repeatpass) || empty($email)) {
    echo "Заполните все поля";
    exit;
}

// Проверка совпадения паролей
if ($pass !== $repeatpass) {
    echo "Пароли не совпадают";
    exit;
}

// Валидация имени пользователя
if (!preg_match('/^[a-zA-Z0-9]{2,32}$/', $login)) {
    echo "Имя пользователя должно содержать от 2 до 32 латинских символов и цифр";
    exit;
}

// Валидация пароля
if (!preg_match('/^(?=.*[A-Z])(?=.*\d)(?=.*[!@#\$%\^&\*])[\w!@#\$%\^&\*]{4,16}$/', $pass)) {
    echo "Пароль должен содержать от 4 до 16 символов, включать заглавную букву, цифру и специальный символ";
    exit;
}

// Проверка, существует ли пользователь
$checkStmt = $conn->prepare("SELECT id FROM users WHERE login = ?");
$checkStmt->bind_param("s", $login);
$checkStmt->execute();
$checkStmt->store_result();

if ($checkStmt->num_rows > 0) {
    echo "Пользователь с таким именем уже существует. Пожалуйста, выберите другое имя.";
    $checkStmt->close();
    $conn->close();
    exit;
}
$checkStmt->close();

// Хеширование пароля
$hashedPass = password_hash($pass, PASSWORD_DEFAULT);

// Сохранение пользователя
$insertStmt = $conn->prepare("INSERT INTO users (login, pass, email) VALUES (?, ?, ?)");
$insertStmt->bind_param("sss", $login, $hashedPass, $email);

if ($insertStmt->execute()) {
    echo "Успешная регистрация";
} else {
    echo "Ошибка при регистрации: " . $insertStmt->error;
}

$insertStmt->close();
$conn->close();