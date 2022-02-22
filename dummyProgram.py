import pandas as pd

# path directory
# dataset = r'D:\LATIHAN PEMROGRAMAN\(TUGAS AKHIR)\XBR_USD Historical Data.csv' # format tanggal menyebalkan
alamat_data = r'D:/LATIHAN PEMROGRAMAN/(TUGAS AKHIR)/Preprocess Logam dan Minyak/csv_format/Brent Oil Futures Historical Data.csv'


# membuat dataframe
df = pd.read_csv(alamat_data, delimiter=";") # 1329 baris, 7 kolom
print(df)

# drop kolom
brent = pd.DataFrame(df).drop(['Open', 'High', 'Low', 'Vol.', 'Change %'], axis=1)

print(brent)
