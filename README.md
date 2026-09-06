# 🚨 Real-Time E-Commerce Fraud Detection & Streaming CDC Pipeline

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://real-time-ecommerce-fraud-detection.streamlit.app/)

> **Note:** The live dashboard on Streamlit Cloud requires a running local infrastructure (PostgreSQL CDC & Kafka Pipeline). For full real-time streaming functionality, please follow the local setup instructions below.

![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)
![Apache Kafka](https://img.shields.io/badge/Apache_Kafka-231F20?style=for-the-badge&logo=apache-kafka&logoColor=white)
![Apache Flink](https://img.shields.io/badge/Apache_Flink-E6526F?style=for-the-badge&logo=apache-flink&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Python](https://img.shields.io/badge/Python_3.12-3776AB?style=for-the-badge&logo=python&logoColor=white)

An enterprise-grade real-time event streaming and fraud detection architecture built with PostgreSQL, Debezium CDC, Apache Kafka, Apache Flink, and Streamlit.

## 🏗️ Architecture Overview

PostgreSQL (OLTP) ──WAL Log──> Debezium (CDC) ──JSON Events──> Apache Kafka ──Stream Query──> Apache Flink SQL ──Live Feed──> Streamlit Dashboard

## 🛠️ Tech Stack
* **Database**: PostgreSQL (OLTP Engine with `REPLICA IDENTITY FULL`)
* **Change Data Capture**: Debezium Connector
* **Event Stream**: Apache Kafka & Zookeeper
* **Stream Processing**: Apache Flink (SQL API)
* **Visualization**: Streamlit & Plotly
* **Language/Tools**: Python 3.12, Docker Compose, SQL

## 🚀 Key Features
* **Change Data Capture (CDC)**: Low-latency log-based ingestion from PostgreSQL Write-Ahead Logs without hurting database performance.
* **Stream Anomaly Filtering**: Sub-second fraud detection using Flink SQL querying high-value transactions (> $5,000).
* **Interactive Operations Dashboard**: Real-time KPI monitoring, transaction scatter analysis, and live high-risk alert logs.

## 🔧 How to Run
1. Start infrastructure: `docker compose up -d`
2. Register Debezium connector via REST API.
3. Start mock transaction stream: `python producer.py`
4. Run live dashboard: `streamlit run app.py`