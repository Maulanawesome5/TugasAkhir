import pandas as pd

# print(gold, silver) # 1322 baris, 1323 baris, 6 kolom
# print(wti, brent) # 1532 baris, 988 baris, 6 kolom

alamat_data = r'D:/LATIHAN PEMROGRAMAN/(TUGAS AKHIR)/Preprocess Logam dan Minyak/csv_format/WTI_USD.csv'

df = pd.read_csv(alamat_data, delimiter=';')
print(df)
