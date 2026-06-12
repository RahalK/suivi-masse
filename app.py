import pandas as pd
import streamlit as st
from datetime import date
from sheets import ajouter_masse, recuperer_donnees

data = recuperer_donnees()
df = pd.DataFrame(data)

df["date"] = pd.to_datetime(df["date"], errors="coerce")
df = df[df["date"].notna()]
df = df.sort_values("date")

df["moyenne_7j"] = df["masse"].rolling(window=7, min_periods=1).mean()

st.title("Suivi de la masse (en kg) de Karen")

st.subheader("Évolution de la masse")

if not df.empty:
    st.line_chart(df.set_index("date")[["masse", "moyenne_7j"]])
else:
    st.info("Aucune donnée pour le moment")

masse = st.number_input("Masse (kg)", min_value=0.0, step=0.1)

if st.button("Ajouter") and masse > 0:
    ajouter_masse(str(date.today()), masse)
    st.success("Ajouté dans Google Sheets ✅")

# ctrl K + ctrl C for comments on pycharm