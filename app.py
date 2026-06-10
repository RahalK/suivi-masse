#import streamlit as st

#st.title("Suivi de la masse (en kg) de Karen")

#poids = st.number_input("Masse (kg)", step=0.1)

#if st.button("Ajouter"):
#    st.write("Tu as entré :", poids)



import streamlit as st
from datetime import date
from sheets import ajouter_poids

st.title("Suivi de la masse (en kg) de Karen")

poids = st.number_input("Masse (kg)", value=None, step=0.1)

# ctrl K + ctrl C for comments on pycharm
# if st.button("Ajouter"):
#     if poids is None:
#         st.error("Veuillez entrer un poids.")
#     else:
#         st.write("Tu as entré :", poids)


if st.button("Ajouter"):
    ajouter_poids(str(date.today()), poids)
    st.success("Ajouté dans Google Sheets ✅")