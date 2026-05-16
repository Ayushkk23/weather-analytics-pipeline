🌦️ Real-Time Weather Analytics Pipeline using Snowflake \& Power BI



A modern end-to-end weather analytics project that combines real-time API ingestion, cloud data warehousing, ETL processing, and interactive business intelligence visualization.



This project fetches live weather and air quality data from WeatherAPI, processes it using Python ETL pipelines, stores it in Snowflake, and visualizes insights through an interactive Power BI dashboard.



🚀 Project Architecture

WeatherAPI

&#x20;   ↓

Python ETL Pipeline

&#x20;   ↓

Snowflake Cloud Data Warehouse

&#x20;   ↓

Power BI Dashboard

📊 Dashboard Preview

Main Dashboard Features

Real-Time Temperature Monitoring

AQI \& Pollution Analysis

Forecast Trends

Rain Probability Insights

Wind Speed, Humidity \& Pressure Monitoring

Sunrise \& Sunset Tracking

✨ Key Features

🔄 Real-time Weather API Integration

☁️ Snowflake Cloud Data Warehouse Integration

🐍 Python-based ETL Pipeline

📈 Interactive Power BI Dashboard

🌍 Multi-location Weather Monitoring

🌫️ Air Quality Index (AQI) Visualization

📅 Forecast Analysis \& Trend Monitoring

🎨 Modern Glassmorphism UI Design

⚡ Automated Data Refresh Workflow

📊 DAX Measures \& Data Modeling

🛠️ Tech Stack

Technology	Purpose

Power BI	Dashboard \& Visualization

Snowflake	Cloud Data Warehouse

Python	ETL Pipeline

WeatherAPI	Real-Time Weather Data

SQL	Database Management

DAX	KPI \& Analytics Calculations

📂 Project Structure

📦 Weather-Analytics-Pipeline

&#x20;┣ 📂 Dashboard

&#x20;┃ ┗ 📄 Weather\_Dashboard.pbix

&#x20;┣ 📂 Python\_ETL

&#x20;┃ ┗ 📄 weather\_etl.py

&#x20;┣ 📂 SQL

&#x20;┃ ┗ 📄 snowflake\_tables.sql

&#x20;┣ 📂 Screenshots

&#x20;┃ ┣ 📄 dashboard\_preview.png

&#x20;┃ ┣ 📄 snowflake\_setup.png

&#x20;┃ ┗ 📄 data\_model.png

&#x20;┣ 📄 README.md

&#x20;┗ 📄 requirements.txt

⚙️ Snowflake Setup

Create Database \& Schema

CREATE DATABASE WEATHER\_DB;



USE DATABASE WEATHER\_DB;



CREATE SCHEMA WEATHER\_SCHEMA;



USE SCHEMA WEATHER\_SCHEMA;

Create Weather Table

CREATE OR REPLACE TABLE CURRENT\_DATA (

&#x20;   CITY STRING,

&#x20;   REGION STRING,

&#x20;   COUNTRY STRING,

&#x20;   TEMP\_C FLOAT,

&#x20;   FEELSLIKE\_C FLOAT,

&#x20;   HUMIDITY FLOAT,

&#x20;   WIND\_KPH FLOAT,

&#x20;   PRESSURE\_MB FLOAT,

&#x20;   PRECIP\_MM FLOAT,

&#x20;   VIS\_KM FLOAT,

&#x20;   UV FLOAT,

&#x20;   AQI\_CO FLOAT,

&#x20;   AQI\_NO2 FLOAT,

&#x20;   AQI\_O3 FLOAT,

&#x20;   AQI\_SO2 FLOAT,

&#x20;   AQI\_PM2\_5 FLOAT,

&#x20;   AQI\_PM10 FLOAT,

&#x20;   LAST\_UPDATED TIMESTAMP

);

🐍 Python ETL Workflow



The ETL script:



Fetches live weather data from WeatherAPI

Extracts weather \& AQI metrics

Connects to Snowflake

Inserts records into cloud tables

Enables real-time analytics in Power BI

📈 Power BI Features

Dynamic KPI Cards

Forecast Trend Analysis

AQI Monitoring

Interactive Filters

Location-based Insights

Custom DAX Measures

Glassmorphism UI Design

📌 Business Use Cases

Environmental Monitoring

Weather Intelligence Reporting

Smart City Analytics

Climate Trend Visualization

Real-Time Data Engineering Practice

🎯 Learning Outcomes



This project demonstrates practical skills in:



Data Engineering

Cloud Warehousing

ETL Pipeline Development

API Integration

Data Modeling

Business Intelligence

Dashboard Design

🔥 Future Improvements

AWS Lambda Automation

Historical Weather Trend Storage

Streamlit Frontend Integration

Automated Alerts for AQI Thresholds

Incremental Data Loading

Real-Time Streaming Pipeline

# 🧠 Developer Notes



This project focuses on integrating real-time API ingestion, ETL processing, cloud-based warehousing, and interactive analytics visualization into a single end-to-end pipeline.

