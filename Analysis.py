import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("CAPSTONEDATA.csv")

st.title("Project Sales Dashboard")

# Sales Line Chart
st.subheader("Net Sales Trend")
data['PROJDATE'] = pd.to_datetime(data['PROJDATE'])
data['YearMonth'] = data['PROJDATE'].dt.to_period('M')
monthly_sales = data.groupby('YearMonth')['NETSALES'].sum().reset_index()
monthly_sales['YearMonth'] = monthly_sales['YearMonth'].astype(str)
st.line_chart(monthly_sales, x="YearMonth", y="NETSALES", color="#800080")

# Gross Sales and Net Sales by Category
st.subheader("Sales by Category")
category_sales = data.groupby('CATEGORY')[['GROSSSALES', 'NETSALES']].sum().reset_index()
st.bar_chart(category_sales, x='CATEGORY', y=['GROSSSALES', 'NETSALES'], color=["#800080", "#be2ed6"])

# Profit After Tax by Country
st.subheader("Profit After Tax by Country")
country_profit = data.groupby('COUNTRY')['PROFITAFTERTAX'].sum().reset_index()
st.bar_chart(country_profit, x='COUNTRY', y='PROFITAFTERTAX', color="#800080")

# Gross Income Distribution
fig, ax = plt.subplots()
st.subheader("Gross Income Distribution")
ax.hist(data['GROSSINCOME'], bins=20, color='purple')
plt.xlabel('Gross Income')
plt.ylabel('Frequency')
plt.title('Distribution of Gross Income')
st.pyplot(fig)

# Project Count by CSAT
st.subheader("Project Count by CSAT")
csat_count = data['CSAT'].value_counts().reset_index()
csat_count.columns = ['CSAT', 'Count']
st.bar_chart(csat_count, x='CSAT', y='Count', color="#800080")

# Additional Information
st.subheader("Additional Information")
st.write("Total Taxable Income: ", data['TOTALTAXABLEINCOME'].sum())
st.write("Retained Earnings: ", data['RETAINEDEARNINGS'].sum())