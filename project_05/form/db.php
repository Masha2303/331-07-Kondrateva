<?php

$servername = "localhost";
$username = "root";
$password = "";
$dbname = "my_database"; // ← укажи реальное имя базы данных

// Подключение
$conn = mysqli_connect($servername, $username, $password, $dbname);

// Проверка подключения
if (!$conn) {
    die("Ошибка подключения: " . mysqli_connect_error());
} else {
    echo "Успешное подключение к базе данных";
}
?>