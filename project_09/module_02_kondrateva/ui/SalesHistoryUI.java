package module_02_gadzhibatyrov.src.ui;

import module_02_gadzhibatyrov.src.DbConnector;
import module_01_gadzhibatyrov.src.ExcelToDB;
import javax.swing.*;
import javax.swing.table.DefaultTableModel;
import java.awt.*;
import java.io.File;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;

public class SalesHistoryUI extends JPanel {
    private final DbConnector db;
    private JTable table;
    private DefaultTableModel tableModel;

    public SalesHistoryUI(DbConnector dbConnector) {
        this.db = dbConnector;
        setLayout(new BorderLayout());

        // **Создаем таблицу с колонками**
        tableModel = new DefaultTableModel();
        tableModel.setColumnIdentifiers(new String[]{"Продукция", "Наименование партнёра", "Количество", "Дата продажи"});
        table = new JTable(tableModel);
        add(new JScrollPane(table), BorderLayout.CENTER);

        // **Кнопка для загрузки данных**
        JButton uploadButton = new JButton("📂 Загрузить историю продаж");
        uploadButton.addActionListener(e -> uploadExcelFile());
        add(uploadButton, BorderLayout.NORTH);

        loadSalesHistoryFromDB(); // **Загружаем данные из БД**

        table = new JTable(tableModel);
        table.setRowHeight(25); // Увеличиваем высоту строк
        table.setFont(new Font("Arial", Font.PLAIN, 14)); // Увеличенный шрифт
        table.setGridColor(Color.LIGHT_GRAY); // Полосы между строками
        table.setSelectionBackground(new Color(173, 216, 230)); // Цвет выделения строк

        JScrollPane scrollPane = new JScrollPane(table);
        scrollPane.setBorder(BorderFactory.createLineBorder(Color.GRAY, 2)); // Рамка вокруг таблицы
        add(scrollPane, BorderLayout.CENTER);

    }

    private void uploadExcelFile() {
        JFileChooser fileChooser = new JFileChooser();
        fileChooser.setDialogTitle("Выберите файл с историей продаж");
        fileChooser.setFileSelectionMode(JFileChooser.FILES_ONLY);

        int result = fileChooser.showOpenDialog(this);
        if (result == JFileChooser.APPROVE_OPTION) {
            File selectedFile = fileChooser.getSelectedFile();
            String filePath = selectedFile.getAbsolutePath();

            try (Connection connection = db.connect()) {
                if (connection != null) {
                    tableModel.setRowCount(0); // 🔹 Очистка таблицы перед импортом

                    boolean success = ExcelToDB.importSalesHistory(connection, filePath);

                    if (success) {
                        loadSalesHistoryFromDB(); // 🔹 Обновляем таблицу после загрузки
                        JOptionPane.showMessageDialog(this, "✅ История продаж загружена!", "Успех", JOptionPane.INFORMATION_MESSAGE);
                    } else {
                        JOptionPane.showMessageDialog(this, "❌ Ошибка: Некорректные данные в файле! Проверьте количество товаров и даты.", "Ошибка загрузки", JOptionPane.ERROR_MESSAGE);
                    }
                } else {
                    JOptionPane.showMessageDialog(this, "❌ Ошибка подключения к базе!", "Ошибка", JOptionPane.ERROR_MESSAGE);
                }
            } catch (Exception e) {
                JOptionPane.showMessageDialog(this, "❌ Ошибка обработки файла: " + e.getMessage(), "Ошибка", JOptionPane.ERROR_MESSAGE);
            }
        }
    }


    private void loadSalesHistoryFromDB() {
        tableModel.setRowCount(0); // Очистка старых данных в GUI

        try (Connection connection = db.connect()) {
            if (connection == null) {
                JOptionPane.showMessageDialog(this, "❌ Ошибка подключения к базе данных!", "Ошибка", JOptionPane.ERROR_MESSAGE);
                return;
            }

            String sql = "SELECT product_name, partner_name, quantity, sale_date FROM sales_history ORDER BY sale_date DESC";
            PreparedStatement stmt = connection.prepareStatement(sql);
            ResultSet rs = stmt.executeQuery();

            while (rs.next()) {
                Object[] row = {
                        rs.getString("product_name"),
                        rs.getString("partner_name"),
                        rs.getInt("quantity"),
                        rs.getDate("sale_date").toString() // Форматирование даты
                };
                tableModel.addRow(row); // Добавляем обновленные данные
            }

            tableModel.fireTableDataChanged(); // Обновляем GUI
            table.repaint();

        } catch (Exception e) {
            JOptionPane.showMessageDialog(this, "❌ Ошибка загрузки истории продаж: " + e.getMessage(), "Ошибка", JOptionPane.ERROR_MESSAGE);
        }
    }
}

