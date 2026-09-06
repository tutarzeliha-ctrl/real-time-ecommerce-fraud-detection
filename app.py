import time
import pandas as pd
import numpy as np
import plotly.express as px
import psycopg2
import streamlit as st

st.set_page_config(
    page_title="Real-Time E-Commerce Fraud Detection",
    page_icon="🚨",
    layout="wide"
)

st.title("🚨 Real-Time E-Commerce Fraud Detection & CDC Dashboard")
st.markdown("PostgreSQL -> Debezium CDC -> Kafka -> Flink -> Streamlit Pipeline")

def get_db_connection():
    return psycopg2.connect(
        host="localhost",
        port="5432",
        database="ecommerce_db",
        user="postgres",
        password="postgrespassword"
    )

def fetch_transactions():
    conn = get_db_connection()
    query = """
    SELECT transaction_id, user_id, amount, payment_method, ip_address, device_id, created_at
    FROM transactions
    ORDER BY created_at DESC
    LIMIT 100;
    """
    df = pd.read_sql(query, conn)
    conn.close()
    return df

def generate_mock_data():
    np.random.seed(42)
    methods = ['CREDIT_CARD', 'DEBIT_CARD', 'PAYPAL', 'CRYPTO']
    data = []
    for i in range(100, 0, -1):
        amount = np.random.choice([np.random.uniform(10, 500), np.random.uniform(5500, 15000)], p=[0.85, 0.15])
        data.append({
            "transaction_id": i,
            "user_id": np.random.randint(100, 999),
            "amount": round(amount, 2),
            "payment_method": np.random.choice(methods),
            "ip_address": "192.168.1.99",
            "created_at": pd.Timestamp.now() - pd.Timedelta(seconds=i*3)
        })
    return pd.DataFrame(data)

placeholder = st.empty()
counter = 0

while True:
    counter += 1
    is_mock = False
    
    try:
        df = fetch_transactions()
    except Exception:
        df = generate_mock_data()
        is_mock = True

    df['is_fraud'] = df['amount'] > 5000
    total_tx = len(df)
    total_amount = df['amount'].sum()
    fraud_df = df[df['is_fraud']]
    fraud_count = len(fraud_df)
    fraud_amount = fraud_df['amount'].sum()
    
    with placeholder.container():
        if is_mock:
            st.warning("⚠️ **Demo Mode Active**: Local database is disconnected. Showing simulated streaming data for UI demonstration.")
        
        kpi1, kpi2, kpi3, kpi4 = st.columns(4)
        kpi1.metric(label="Total Transactions (Last 100)", value=total_tx)
        kpi2.metric(label="Total Volume", value=f"${total_amount:,.2f}")
        kpi3.metric(label="🚨 Fraud Alerts", value=fraud_count, delta_color="inverse")
        kpi4.metric(label="⚠️ Fraud Volume", value=f"${fraud_amount:,.2f}")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Transaction Amount Distribution & Anomalies")
            fig_scatter = px.scatter(
                df, 
                x="created_at", 
                y="amount", 
                color="is_fraud",
                color_discrete_map={True: "red", False: "green"},
                hover_data=["transaction_id", "user_id", "payment_method", "ip_address"],
                title="Real-Time Transaction Stream"
            )
            st.plotly_chart(fig_scatter, use_container_width=True, key=f"scatter_{counter}")
            
        with col2:
            st.subheader("Fraud Count by Payment Method")
            if not fraud_df.empty:
                method_counts = fraud_df['payment_method'].value_counts().reset_index()
                method_counts.columns = ['payment_method', 'count']
                fig_bar = px.bar(
                    method_counts, 
                    x='payment_method', 
                    y='count', 
                    color='payment_method',
                    title="Suspicious Transactions by Method"
                )
                st.plotly_chart(fig_bar, use_container_width=True, key=f"bar_{counter}")
            else:
                st.info("No fraud detected in the current window.")

        st.subheader("📋 Live High-Risk Transactions Log (> $5,000)")
        if not fraud_df.empty:
            st.dataframe(
                fraud_df[['transaction_id', 'user_id', 'amount', 'payment_method', 'ip_address', 'created_at']], 
                use_container_width=True
            )
        else:
            st.write("No high-risk transactions detected.")
            
    time.sleep(2)