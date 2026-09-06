# 🚨 Real-Time E-Commerce Fraud Detection & Streaming CDC Pipeline

An enterprise-grade real-time event streaming and fraud detection architecture built with PostgreSQL, Debezium, Apache Kafka, Apache Flink, and Streamlit.

## 🏗️ Architecture Overview

PostgreSQL (Source DB) ──WAL──> Debezium (CDC) ──JSON──> Apache Kafka (Event Bus) ──Stream Processing──> Apache Flink (Fraud Detection) ──Live Visualization──> Streamlit Dashboard

## 🛠️ Tech Stack
* **Database**: PostgreSQL (OLTP)
* **CDC Engine**: Debezium Connector
* **Event Stream**: Apache Kafka
* **Stream Engine**: Apache Flink (SQL)
* **Visualization**: Streamlit & Plotly
* **Language**: Python 3.12 / SQL

## 🚀 Key Features
* **Change Data Capture (CDC)**: Low-latency log-based ingestion from PostgreSQL Write-Ahead Logs (WAL) using `REPLICA IDENTITY FULL`.
* **Real-Time Anomaly Detection**: Flink SQL pipeline filtering high-risk transactions (> $5,000) with sub-second latency.
* **Interactive Monitoring**: Streamlit dashboard rendering live metrics, distribution scatter plots, and fraud logs.

## 🔧 How to Run
1. Start infrastructure: `docker compose up -d`
2. Register Debezium connector via REST API.
3. Start mock transactions: `python producer.py`
4. Run live dashboard: `streamlit run app.py`