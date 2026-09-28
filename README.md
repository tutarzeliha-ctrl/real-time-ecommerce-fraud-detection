# 🚨 Real-Time E-Commerce Fraud Detection & Streaming CDC Pipeline

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://real-time-ecommerce-fraud-detection-rnvcakjvrf6crud4syg6a2.streamlit.app)

> **Note:** The live dashboard on Streamlit Cloud requires the local streaming infrastructure (PostgreSQL CDC, Kafka, Flink) running on `localhost`. Please follow the setup instructions below to run the complete pipeline locally.

![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)
![Apache Kafka](https://img.shields.io/badge/Apache_Kafka-231F20?style=for-the-badge&logo=apache-kafka&logoColor=white)
![Apache Flink](https://img.shields.io/badge/Apache_Flink-E6526F?style=for-the-badge&logo=apache-flink&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Python](https://img.shields.io/badge/Python_3.12-3776AB?style=for-the-badge&logo=python&logoColor=white)

An enterprise-grade real-time event streaming and fraud detection architecture built with PostgreSQL, Debezium CDC, Apache Kafka, Apache Flink, and Streamlit.

---

## 🏗️ Architecture Overview

```text
PostgreSQL (OLTP) ──WAL Log──> Debezium (CDC) ──JSON Events──> Apache Kafka ──Stream Query──> Apache Flink SQL ──Live Feed──> Streamlit Dashboard
🛠️ Tech StackDatabase: PostgreSQL (OLTP Engine with REPLICA IDENTITY FULL)Change Data Capture: Debezium ConnectorEvent Stream: Apache Kafka & ZookeeperStream Processing: Apache Flink (SQL API)Visualization: Streamlit & PlotlyLanguage/Tools: Python 3.12, Docker Compose, SQL🚀 Key FeaturesChange Data Capture (CDC): Low-latency log-based ingestion from PostgreSQL Write-Ahead Logs without hurting database performance.Stream Anomaly Filtering: Sub-second fraud detection using Flink SQL querying high-value transactions (> $5,000).Interactive Operations Dashboard: Real-time KPI monitoring, transaction scatter analysis, and live high-risk alert logs.⚙️ Overcoming Engineering ChallengesBuilding robust real-time streaming architectures comes with deep infrastructure hurdles. Here is how key bottlenecks were resolved during development:StageChallengeSolution1. Environment & DockerizationJava version mismatches, JAVA_HOME path errors, and spark-class execution failures inside containers.Standardized the base runtime using Eclipse Temurin 17 JDK (eclipse-temurin:17-jdk-jammy) and configured explicit symlinks.2. Event Streaming & NetworkInternal Docker DNS resolution errors (Name or service not known on kafka:9092) and dynamic dependency fetching.Configured optimized Docker bridge networking (kafka:9092) and managed automated package caching.3. Stream Processing & SinkLow-latency state management and real-time schema enforcement across streaming nodes.Implemented robust JSON parsing, schema validation rules, and reliable batch sinks.🔧 How to RunStart infrastructure: docker compose up -dRegister Debezium connector via REST API.Start mock transaction stream: python producer.pyRun live dashboard: streamlit run app.pyCreated by Zeliha Tutar