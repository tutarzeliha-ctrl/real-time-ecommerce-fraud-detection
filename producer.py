import time
import random
from faker import Faker
import psycopg2

fake = Faker()

# Database Connection Settings
conn = psycopg2.connect(
    host="localhost",
    port="5432",
    database="ecommerce_db",
    user="postgres",
    password="postgrespassword"
)
cursor = conn.cursor()

payment_methods = ['CREDIT_CARD', 'DEBIT_CARD', 'PAYPAL', 'CRYPTO']

print("🚀 Real-Time Transaction Data Producer Started... (Press Ctrl+C to stop)")

try:
    while True:
        # Generate a fraud transaction with 10% probability
        is_fraud = random.random() < 0.10
        
        user_id = random.randint(1, 3)
        amount = round(random.uniform(5000, 15000), 2) if is_fraud else round(random.uniform(10, 500), 2)
        payment_method = random.choice(payment_methods)
        ip_address = "192.168.1.99" if is_fraud else fake.ipv4()
        device_id = "SUSPICIOUS_DEVICE_X" if is_fraud else fake.uuid4()

        insert_query = """
        INSERT INTO transactions (user_id, amount, payment_method, ip_address, device_id)
        VALUES (%s, %s, %s, %s, %s) RETURNING transaction_id;
        """
        cursor.execute(insert_query, (user_id, amount, payment_method, ip_address, device_id))
        conn.commit()
        
        tx_id = cursor.fetchone()[0]
        status_tag = "⚠️ [FRAUD ANOMALY]" if is_fraud else "✅ [NORMAL]"
        print(f"{status_tag} Tx ID: {tx_id} | User: {user_id} | Amount: ${amount} | IP: {ip_address}")
        
        # Wait randomly between 1 and 3 seconds
        time.sleep(random.uniform(1, 3))

except KeyboardInterrupt:
    print("\n🛑 Data generation stopped by user.")
    cursor.close()
    conn.close()