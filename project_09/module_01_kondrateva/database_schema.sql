
-- Таблица: partners (Партнёры)
CREATE TABLE partners (
    partner_id SERIAL PRIMARY KEY,
    type VARCHAR(50),
    company_name VARCHAR(100) NOT NULL,
    legal_address TEXT,
    inn VARCHAR(12),
    director_name VARCHAR(100),
    contact_phone VARCHAR(20),
    contact_email VARCHAR(100),
    rating INTEGER,
    logo TEXT
);

-- Таблица: sale_locations (Места продаж)
CREATE TABLE sale_locations (
    location_id SERIAL PRIMARY KEY,
    partner_id INTEGER NOT NULL REFERENCES partners(partner_id) ON DELETE CASCADE,
    address TEXT NOT NULL
);

-- Таблица: sales_history (История реализаций)
CREATE TABLE sales_history (
    history_id SERIAL PRIMARY KEY,
    partner_id INTEGER NOT NULL REFERENCES partners(partner_id) ON DELETE CASCADE,
    product_name VARCHAR(100) NOT NULL,
    sale_date DATE NOT NULL,
    quantity INTEGER NOT NULL,
    total_price NUMERIC(12, 2) NOT NULL
);
