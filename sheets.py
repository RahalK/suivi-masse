import gspread
from google.oauth2.service_account import Credentials

# SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

creds = Credentials.from_service_account_file(
    "credentials.json",
    scopes=SCOPES
)

client = gspread.authorize(creds)

sheet = client.open("Suivi_masse_Karen").sheet1

def ajouter_poids(date, masse):
    sheet.append_row([date, masse])
