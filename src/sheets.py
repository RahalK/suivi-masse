import streamlit as st
import gspread
from google.oauth2.service_account import Credentials

# SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

creds = Credentials.from_service_account_info(
    st.secrets["google_service_account"],
    scopes=SCOPES
)

client = gspread.authorize(creds)

sheet = client.open("Suivi_masse_Karen").sheet1

def ajouter_masse(date, masse):
    sheet.append_row([date, masse])

def recuperer_donnees():
    data = sheet.get_all_records()
    return data
