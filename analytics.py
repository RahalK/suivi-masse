import pandas as pd

def preparer_donnees(data):
    df = pd.DataFrame(data)

    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df = df[df["date"].notna()]
    df = df.sort_values("date")

    df["moyenne_7j"] = df["masse"].rolling(window=7, min_periods=1).mean()

    return df