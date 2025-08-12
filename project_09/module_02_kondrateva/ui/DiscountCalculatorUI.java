package module_02_gadzhibatyrov.src.ui;

import module_02_gadzhibatyrov.src.DbConnector;
import javax.swing.*;
import java.awt.*;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.util.ArrayList;

public class DiscountCalculatorUI extends JPanel {
    private JComboBox<String> partnerDropdown, productDropdown; // Выпадающие меню
    private JTextField totalSalesField;
    private JLabel discountLabel;
    private JButton calculateButton, updateButton;

    public DiscountCalculatorUI(DbConnector db) {
        setLayout(new GridLayout(5, 2, 10, 10));

        JLabel partnerLabel = new JLabel("Выберите партнёра:");
        partnerDropdown = new JComboBox<>(loadPartnersFromDB());
        partnerDropdown.addActionListener(e -> updateProductDropdown()); //Обновляем список продукции

        JLabel productLabel = new JLabel("Выберите продукцию:");
        productDropdown = new JComboBox<>();

        JLabel salesLabel = new JLabel("Общий объём продаж:");
        totalSalesField = new JTextField();

        JLabel discountTextLabel = new JLabel("Индивидуальная скидка:");
        discountLabel = new JLabel("0%");

        calculateButton = new JButton("Рассчитать скидку");
        updateButton = new JButton("Обновить данные");

        calculateButton.addActionListener(e -> calculateDiscount());
        updateButton.addActionListener(e -> updateDatabase());

        add(partnerLabel);
        add(partnerDropdown);
        add(productLabel);
        add(productDropdown);
        add(salesLabel);
        add(totalSalesField);
        add(discountTextLabel);
        add(discountLabel);
        add(calculateButton);
        add(updateButton);
    }

    private String[] loadPartnersFromDB() {
        ArrayList<String> partners = new ArrayList<>();
        try (Connection conn = module_02_gadzhibatyrov.src.DbConnector.connect()) {
            String sql = "SELECT DISTINCT partner_name FROM sales_history";
            PreparedStatement stmt = conn.prepareStatement(sql);
            ResultSet rs = stmt.executeQuery();

            while (rs.next()) {
                partners.add(rs.getString("partner_name"));
            }
        } catch (Exception e) {
            JOptionPane.showMessageDialog(this, "❌ Ошибка загрузки партнёров: " + e.getMessage(), "Ошибка", JOptionPane.ERROR_MESSAGE);
        }

        if (partners.isEmpty()) {
            partners.add("Нет доступных партнёров"); //Если список пуст
        }

        return partners.toArray(new String[0]);
    }

    private void updateProductDropdown() {
        String selectedPartner = (String) partnerDropdown.getSelectedItem();
        if (selectedPartner == null || selectedPartner.equals("Нет доступных партнёров")) {
            return;
        }

        productDropdown.removeAllItems(); // чищаем старые данные

        try (Connection conn = module_02_gadzhibatyrov.src.DbConnector.connect()) {
            String sql = "SELECT DISTINCT product_name FROM sales_history WHERE partner_name = ?";
            PreparedStatement stmt = conn.prepareStatement(sql);
            stmt.setString(1, selectedPartner);
            ResultSet rs = stmt.executeQuery();

            while (rs.next()) {
                productDropdown.addItem(rs.getString("product_name"));
            }

            if (productDropdown.getItemCount() == 0) {
                productDropdown.addItem("Нет доступных товаров");
            }

        } catch (Exception e) {
            JOptionPane.showMessageDialog(this, "❌ Ошибка загрузки продукции: " + e.getMessage(), "Ошибка", JOptionPane.ERROR_MESSAGE);
        }
    }

    private void calculateDiscount() {
        try {
            int totalSales = Integer.parseInt(totalSalesField.getText());
            float discount = calculateDiscountRate(totalSales);
            discountLabel.setText(discount + "%");
        } catch (NumberFormatException e) {
            JOptionPane.showMessageDialog(this, "❌ Ошибка! Введите корректное число.", "Ошибка", JOptionPane.ERROR_MESSAGE);
        }
    }

    private float calculateDiscountRate(int totalSales) {
        if (totalSales < 10_000) return 0.0f;
        if (totalSales < 50_000) return 5.0f;
        if (totalSales < 300_000) return 10.0f;
        return 15.0f;
    }

    private void updateDatabase() {
        try (Connection conn = module_02_gadzhibatyrov.src.DbConnector.connect()) {
            conn.setAutoCommit(false);
            String selectedPartner = (String) partnerDropdown.getSelectedItem();
            String selectedProduct = (String) productDropdown.getSelectedItem();
            int totalSales = Integer.parseInt(totalSalesField.getText());
            float discount = calculateDiscountRate(totalSales);

            String checkSql = "SELECT COUNT(*) FROM rate WHERE name = ?";
            PreparedStatement checkStmt = conn.prepareStatement(checkSql);
            checkStmt.setString(1, selectedPartner);
            ResultSet rs = checkStmt.executeQuery();
            rs.next();

            if (rs.getInt(1) > 0) {
                // Партнёр уже есть — обновляем данные
                String updateSql = "UPDATE rate SET total_sales = ?, discount_rate = ? WHERE name = ?";
                PreparedStatement updateStmt = conn.prepareStatement(updateSql);
                updateStmt.setInt(1, totalSales);
                updateStmt.setFloat(2, discount);
                updateStmt.setString(3, selectedPartner);
                updateStmt.executeUpdate();
                System.out.println("✅ Данные обновлены!");
                conn.commit();
            } else {
                // 🔹 Если партнёр отсутствует — создаём новую запись
                String insertSql = "INSERT INTO rate (name, total_sales, discount_rate) VALUES (?, ?, ?)";
                PreparedStatement insertStmt = conn.prepareStatement(insertSql);
                insertStmt.setString(1, selectedPartner);
                insertStmt.setInt(2, totalSales);
                insertStmt.setFloat(3, discount);
                insertStmt.executeUpdate();
                System.out.println("✅ Новый партнёр добавлен!");
                conn.commit();
            }
            JOptionPane.showMessageDialog(this, "✅ Данные обновлены!", "Успех", JOptionPane.INFORMATION_MESSAGE);
        } catch (Exception e) {
            JOptionPane.showMessageDialog(this, "❌ Ошибка обновления данных: " + e.getMessage(), "Ошибка", JOptionPane.ERROR_MESSAGE);
        }
    }
}
