import streamlit as st
from datetime import date
import matplotlib.pyplot as plt

from src.sheets import ajouter_masse, recuperer_donnees
from src.analytics import preparer_donnees


def main():

    data = recuperer_donnees()
    df = preparer_donnees(data)

    st.title("Suivi de la masse (en kg) de Karen")

    if not df.empty:

        fig, ax = plt.subplots()

        ax.plot(df["date"], df["masse"], marker="o", label="Masse")
        ax.plot(df["date"], df["moyenne_7j"], label="Moyenne mobile (7 jours)")

        ax.set_title("Évolution de la masse")
        # ax.set_xlabel("Date")
        ax.set_ylabel("Masse (kg)")
        ax.set_ylim(55, 58)
        plt.xticks(rotation=15)

        ax.legend()

        st.pyplot(fig)

    else:
        st.info("Aucune donnée pour le moment")

    masse = st.number_input("Masse (kg)", min_value=0.0, step=0.1)

    if st.button("Ajouter") and masse > 0:
        ajouter_masse(str(date.today()), masse)
        st.success("Ajouté dans Google Sheets ✅")


if __name__ == "__main__":
    main()