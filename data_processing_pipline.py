# Import necessary libraries
import pandas as pd
import requests
import sqlite3

# Extract Phase

def extract_data():
    # Extract Macroeconomic Indicators
    economic_indicators_df = pd.read_csv("data/indicators.csv", encoding='utf-8')
    
    # Extract FDI Data using World Bank API
    fdi_data_url = "https://api.worldbank.org/v2/country/all/indicator/BX.KLT.DINV.CD.WD?format=json&per_page=1000"
    response = requests.get(fdi_data_url)
    if response.status_code == 200:
        fdi_data = response.json()
        if len(fdi_data) > 1:
            fdi_df = pd.json_normalize(fdi_data[1])
    else:
        fdi_df = pd.DataFrame()  # Handle errors appropriately

    # Extract Logistics Performance Index (LPI)
    lpi_df = pd.read_excel("data/International_LPI_from_2007_to_2023_0.xlsx")

    # Extract Trade Flow Data (Goods and Services)
    goods_trade_df = pd.read_csv("data/Goods UN Comtrade data_11_15_2024_11_6_8.csv", encoding='latin1', on_bad_lines='skip')
    services_trade_df = pd.read_csv("data/servicesun comtrade_data11_15_2024_11_14_7.csv", encoding='latin1', on_bad_lines='skip')

    # Extract Tariff and NTM Data
    ntm_data_df = pd.read_csv("data/NTM-Indicators-Measure-Sector.csv", encoding='latin1', on_bad_lines='skip')

    return economic_indicators_df, fdi_df, lpi_df, goods_trade_df, services_trade_df, ntm_data_df

# Transform Phase

def transform_data(economic_indicators_df, fdi_df, lpi_df, goods_trade_df, services_trade_df, ntm_data_df):
    # Data Cleaning
    # Standardize column names across datasets
    economic_indicators_df.rename(columns={"Country": "country_code", "Year": "year"}, inplace=True)
    economic_indicators_df["year"] = pd.to_numeric(economic_indicators_df["year"], errors='coerce')
    
    # Drop unnecessary columns from FDI data
    fdi_df_cleaned = fdi_df.drop(columns=["unit", "obs_status", "decimal", "indicator.id", "country.id"], errors='ignore')
    fdi_df_cleaned.rename(columns={
        "countryiso3code": "country_code", 
        "date": "year", 
        "value": "fdi_value_usd",
        "indicator.value": "indicator_description",
        "country.value": "country_name"
    }, inplace=True)
    
    # Convert appropriate columns to numeric types
    fdi_df_cleaned["year"] = pd.to_numeric(fdi_df_cleaned["year"], errors='coerce')
    fdi_df_cleaned["fdi_value_usd"] = pd.to_numeric(fdi_df_cleaned["fdi_value_usd"], errors='coerce')
    
    # Merge Datasets
    # Merging Economic Indicators and FDI Data
    integrated_df = pd.merge(economic_indicators_df, fdi_df_cleaned, on=["country_code", "year"], how="left")
    
    # Additional transformations, column pruning, and normalization
    integrated_df.drop(columns=["unit", "obs_status"], errors='ignore', inplace=True)
    integrated_df = integrated_df.infer_objects()  # Infer better data types
    integrated_df.fillna(0, inplace=True)  # Replace missing values with 0 or appropriate values

    return integrated_df

# Load Phase

def load_data(integrated_df):
    # Load to SQLite database
    conn = sqlite3.connect("sme_market_entry_navigator.db")
    integrated_df.to_sql("market_data", conn, if_exists="replace", index=False)
    conn.close()
    
    # Export to CSV as a backup
    integrated_df.to_csv("integrated_market_data.csv", index=False)

# Complete ETL Pipeline Function
def etl_pipeline():
    # Extract
    economic_indicators_df, fdi_df, lpi_df, goods_trade_df, services_trade_df, ntm_data_df = extract_data()
    
    # Transform
    integrated_df = transform_data(economic_indicators_df, fdi_df, lpi_df, goods_trade_df, services_trade_df, ntm_data_df)
    
    # Load
    load_data(integrated_df)

# Execute the ETL Pipeline
if __name__ == "__main__":
    etl_pipeline()
