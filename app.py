import pandas as pd
import streamlit as st
from datetime import date
from sheets import ajouter_masse, recuperer_donnees
from analytics import preparer_donnees

data = recuperer_donnees()
df = preparer_donnees(data)

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