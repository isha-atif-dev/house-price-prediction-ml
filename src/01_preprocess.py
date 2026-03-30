# preprocessing pipeline
import pandas as pd

df = pd.read_csv("../data/raw/Housing.csv")

binary_col = [
    "mainroad",
    "guestroom",
    "basement",
    "hotwaterheating",
    "airconditioning",
    "prefarea"
]

