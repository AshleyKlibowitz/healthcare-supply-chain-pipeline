# Healthcare Supply Chain Pipeline

**Python | Snowflake | Streamlit | ETL | HIPAA Compliance**

### 👤 Persona: Data Engineer
**Gaps Filled:** PII Scrubbing (Security), Cloud Warehousing (Snowflake), Data Modeling (Star Schema), Python Web Apps (Streamlit).

---

### 🏥 The Concept: "Medi-Track"
**A HIPAA-compliant logistics pipeline tracking medical device shipments.**

Real-world healthcare supply chains face two major hurdles: strict data privacy laws (HIPAA) and urgent delivery timelines. This project builds an end-to-end pipeline that ingests raw shipping logs, anonymizes sensitive patient data using cryptographic hashing, warehouses the data in the cloud, and serves a real-time dashboard for hospital inventory managers.

---

### 🏗️ Architecture
**Raw Data (CSV)** $\rightarrow$ **Python (SHA-256 Security Layer)** $\rightarrow$ **Snowflake (Data Warehouse)** $\rightarrow$ **SQL (Transformation)** $\rightarrow$ **Streamlit (App)**

---

### 📊 Dashboard Preview

<img width="853" height="827" alt="Screenshot 2026-01-18 at 2 45 14 PM" src="https://github.com/user-attachments/assets/7a869a3d-6ff2-47e8-a4ca-373fa8ed9073" />

*(The Streamlit interface visualizing real-time delivery status by hospital)*

---

### 🚀 Step-by-Step Breakdown

#### Phase 1: Security & Ingestion (Python)
Before data ever touches the cloud, it must be sanitized. I wrote a Python script using the `faker` and `pandas` libraries to generate realistic shipping manifests.
* **The Problem:** Raw logs contain "Patient Names," which is PII (Personally Identifiable Information).
* **The Solution:** Implemented a **SHA-256 hashing algorithm** to irreversibly scramble names while maintaining referential integrity for analytics.
* *File:* `generate_and_scrub.py`

#### Phase 2: The Data Warehouse (Snowflake)
Data is loaded into a **Snowflake** infrastructure designed for scale.
* **Storage:** `COMPUTE_WH` warehouse and `MEDITRACK_DB` database.
* **Schema:** `SUPPLY_CHAIN` schema to organize tables logically.
* **Ingestion:** Automated loading of the scrubbed CSV into the `SHIPMENTS` table using Snowflake's optimized file loading protocols.

#### Phase 3: Transformation (SQL Modeling)
Raw shipping data is meaningless without context. I used SQL to transform the flat files into a relational **Star Schema**.
* **Dimension Table:** Created a `HOSPITALS` table with metadata (City, Region).
* **Fact Table:** Enriched the `SHIPMENTS` table by joining it with hospital records using generated UUIDs.
* **Business Logic:** Calculated "Late" vs. "On-Time" delivery metrics via SQL aggregation.

#### Phase 4: The Application (Streamlit)
To make the data accessible to non-technical stakeholders, I built a frontend application using **Streamlit**.
* **Connectivity:** Uses `snowflake-connector-python` to fetch live data from the warehouse.
* **Visualization:** Displays KPIs (Total Shipments, Delayed Orders) and bar charts showing delivery status by hospital location.
* *File:* `app.py`

---

### 🛠 Key Skills Demonstrated
* **Data Security:** Implementing SHA-256 hashing for PII/HIPAA compliance.
* **ETL Pipeline:** Extracting, transforming, and loading data using Python.
* **Cloud Engineering:** Managing Snowflake warehouses, databases, and schemas.
* **Data Modeling:** Designing relational tables (Joins, Primary/Foreign Keys).
* **Full-Stack Data:** Building a user-facing frontend to visualize backend data.

---

### 💻 How to Run This Project

**1. Install Dependencies**
```bash
pip install -r requirements.txt
```

### 2. Generate & Scrub Data Run the script to create the raw and sanitized datasets:

python generate_and_scrub.py


### 3. Launch the Dashboard Start the Streamlit application to view the live analytics:

streamlit run app.py
