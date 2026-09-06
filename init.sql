
CREATE TABLE IF NOT EXISTS users (
    user_id SERIAL PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    country VARCHAR(50) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


CREATE TABLE IF NOT EXISTS transactions (
    transaction_id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(user_id),
    amount DECIMAL(10, 2) NOT NULL,
    currency VARCHAR(10) DEFAULT 'USD',
    payment_method VARCHAR(50) NOT NULL,
    ip_address VARCHAR(45) NOT NULL,
    device_id VARCHAR(100) NOT NULL,
    status VARCHAR(20) DEFAULT 'COMPLETED',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


ALTER TABLE users REPLICA IDENTITY FULL;
ALTER TABLE transactions REPLICA IDENTITY FULL;


INSERT INTO users (full_name, email, country) VALUES
('Zeliha Tutar', 'zeliha@example.com', 'TR'),
('John Doe', 'john@example.com', 'US'),
('Alice Smith', 'alice@example.com', 'DE');