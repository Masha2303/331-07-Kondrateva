// JavaScript для модуля 03
document.addEventListener('DOMContentLoaded', function() {
    console.log('Модуль 03 загружен');
    
    // Анимация элементов
    const sections = document.querySelectorAll('.info-section');
    sections.forEach((section, index) => {
        section.style.opacity = '0';
        setTimeout(() => {
            section.style.transition = 'opacity 0.6s ease';
            section.style.opacity = '1';
        }, index * 200);
    });
    
    // Добавление кнопок действий
    addActionButtons();
});

function addActionButtons() {
    const container = document.querySelector('.container');
    if (!container) return;
    
    const buttonSection = document.createElement('div');
    buttonSection.className = 'info-section';
    buttonSection.innerHTML = `
        <h2>Быстрые действия</h2>
        <div style="display: flex; gap: 15px; flex-wrap: wrap;">
            <button class="btn" onclick="showMessage('Запуск приложения...')">🚀 Запустить</button>
            <button class="btn" onclick="showMessage('Открытие документации...')">📖 Документация</button>
        </div>
    `;
    
    // Стили для кнопок
    const style = document.createElement('style');
    style.textContent = `
        .btn {
            padding: 12px 20px;
            border: none;
            border-radius: 5px;
            background: #3498db;
            color: white;
            cursor: pointer;
            transition: all 0.3s ease;
        }
        .btn:hover {
            background: #2980b9;
            transform: translateY(-2px);
        }
    `;
    document.head.appendChild(style);
    
    container.appendChild(buttonSection);
}

function showMessage(message) {
    alert(message);
}
