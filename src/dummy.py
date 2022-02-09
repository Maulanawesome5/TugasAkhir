import pandas as pd
from logam import gold, silver
from minyak import wti, brent

# print(gold, silver) # 1322 baris, 1323 baris, 6 kolom
# print(wti, brent) # 1532 baris, 988 baris, 6 kolom
"""
closing_gold_price = gold.drop(
    ["Open", "High", "Low", "Change %"],
    axis=1
).sort_values(by="Date", ascending=True, ignore_index=True)

closing_silver_price = silver.drop(
    ["Open", "High", "Low", "Change %"],
    axis=1
).sort_values(by="Date",ascending=True,ignore_index=True)

closing_wti_price = wti.drop(
    ["Open", "High", "Low", "Change %"],
    axis=1
).sort_values(by="Date", ascending=True, ignore_index=True)

closing_brent_price = brent.drop(
    ["Open", "High", "Low", "Change %"],
    axis=1
).sort_values(by="Date", ascending=True, ignore_index=True)
"""

# print(closing_gold_price, "\n", closing_silver_price)

alamat_data = r'D:/LATIHAN PEMROGRAMAN/(TUGAS AKHIR)/Preprocess Logam dan Minyak/csv_format/WTI_USD.csv'

df = pd.read_csv(alamat_data, delimiter=';')
print(df)
