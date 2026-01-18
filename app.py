import streamlit as st
import snowflake.connector
import pandas as pd

# 1. Title and Intro
st.title("🏥 Medi-Track: Supply Chain Dashboard")
st.markdown("Real-time tracking of medical supplies across hospital networks.")

# 2. Connect to Snowflake
# UPDATE THESE 3 LINES WITH YOUR DETAILS:
conn = snowflake.connector.connect(
    user='YOUR_USERNAME',        # Your Snowflake login email or username
    password='YOUR_PASSWORD',    # Your Snowflake password
    account='YOUR_ACCOUNT_ID',   # Example: xy12345.us-east-1
    warehouse='COMPUTE_WH',
    database='MEDITRACK_DB',
    schema='SUPPLY_CHAIN'
)

# 3. The Query
query = """
SELECT 
    h.HospitalName,
    h.City,
    s.DeliveryStatus,
    COUNT(s.ShipmentID) as Total_Shipments
FROM SHIPMENTS s
JOIN HOSPITALS h ON s.HospitalID = h.HospitalID
GROUP BY h.HospitalName, h.City, s.DeliveryStatus
ORDER BY Total_Shipments DESC;
"""

# 4. Run Query & Cache Data
@st.cache_data
def load_data():
    cur = conn.cursor()
    cur.execute(query)
    # Fetch result into a pandas DataFrame
    df = cur.fetch_pandas_all()
    return df

# 5. Display the Data
try:
    df = load_data()
    
    # Key Metrics (Top Row)
    total_shipments = df['TOTAL_SHIPMENTS'].sum()
    st.metric(label="Total Shipments Tracked", value=total_shipments)

    # The Table
    st.subheader("📋 Hospital Delivery Status")
    st.dataframe(df)

    # A Simple Bar Chart
    st.subheader("📊 Delivery Issues by Hospital")
    st.bar_chart(df, x="HOSPITALNAME", y="TOTAL_SHIPMENTS", color="DELIVERYSTATUS")

except Exception as e:
    st.error(f"Connection Error: {e}")
