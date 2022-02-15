import pandas as pd

# path directory
# alamat_data = r'D:/LATIHAN PEMROGRAMAN/(TUGAS AKHIR)/Preprocess Logam dan Minyak'
gold_data = r'D:\LATIHAN PEMROGRAMAN\(TUGAS AKHIR)\Preprocess Logam dan Minyak\XAU_USD.xlsx'
silver_data = r'D:\LATIHAN PEMROGRAMAN\(TUGAS AKHIR)\Preprocess Logam dan Minyak\XAG_USD.xlsx'

# dataframe
gold = pd.read_excel(gold_data)
silver = pd.read_excel(silver_data)

# Cara drop tabel dan sortir sesuai urutan tanggal
# mengambil tanggal dan harga close saja
closing_gold_price = gold.drop(
    ["Open", "High", "Low", "Change %"],
    axis=1
).sort_values(by="Date", ascending=True, ignore_index=True)

closing_silver_price = silver.drop(
    ["Open", "High", "Low", "Change %"],
    axis=1
).sort_values(by="Date",ascending=True,ignore_index=True)

# print(gold)
# print(silver)

