# Live Metrics & Visualization Layout
placeholder = st.empty()
counter = 0  # Dynamic key generator counter

while True:
    counter += 1
    
    try:
        df = fetch_transactions()
    except Exception as e:
        with placeholder.container():
            st.error("⚠️ Local Database Connection Required")
            st.warning(
                "This live demo requires the local streaming infrastructure (PostgreSQL CDC, Kafka, Flink) running on localhost. "
                "Please clone the repository and run `docker compose up -d` for full operational functionality."
            )
            st.info("💡 See project README on GitHub for local setup instructions.")
        time.sleep(10)
        continue

    # Fraud Analysis (Transactions above $5000)
    df['is_fraud'] = df['amount'] > 5000
    total_tx = len(df)
    total_amount = df['amount'].sum()
    fraud_df = df[df['is_fraud']]
    fraud_count = len(fraud_df)
    fraud_amount = fraud_df['amount'].sum()
    
    with placeholder.container():
        # KPI Metrics
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