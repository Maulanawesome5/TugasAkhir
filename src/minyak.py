<<<<<<< HEAD
import pandas as pd

# path directory
# alamat_data = r'D:/LATIHAN PEMROGRAMAN/(TUGAS AKHIR)/Preprocess Logam dan Minyak'
wti_data = r'D:\LATIHAN PEMROGRAMAN\(TUGAS AKHIR)\Preprocess Logam dan Minyak\WTI_USD.xlsx'
brent_data = r'D:\LATIHAN PEMROGRAMAN\(TUGAS AKHIR)\Preprocess Logam dan Minyak\XBR_USD.xlsx'

# dataframe
wti = pd.read_excel(wti_data)
brent = pd.read_excel(brent_data)

# Cara drop tabel dan sortir sesuai urutan tanggal
# mengambil tanggal dan harga close saja
closing_wti_price = wti.drop(
    ["Open", "High", "Low", "Change %"],
    axis=1
).sort_values(by="Date", ascending=True, ignore_index=True)

closing_brent_price = brent.drop(
    ["Open", "High", "Low", "Change %"],
    axis=1
).sort_values(by="Date", ascending=True, ignore_index=True)

# print(wti)
# print(brent)

=======
import pandas as pd

# path directory
# alamat_data = r'D:/LATIHAN PEMROGRAMAN/(TUGAS AKHIR)/Preprocess Logam dan Minyak'
wti_data = r'D:\LATIHAN PEMROGRAMAN\(TUGAS AKHIR)\Preprocess Logam dan Minyak\WTI_USD.xlsx'
brent_data = r'D:\LATIHAN PEMROGRAMAN\(TUGAS AKHIR)\Preprocess Logam dan Minyak\XBR_USD.xlsx'

# dataframe
wti = pd.read_excel(wti_data)
brent = pd.read_excel(brent_data)

# Cara drop tabel dan sortir sesuai urutan tanggal
# mengambil tanggal dan harga close saja
closing_wti_price = wti.drop(
    ["Open", "High", "Low", "Change %"],
    axis=1
).sort_values(by="Date", ascending=True, ignore_index=True)

closing_brent_price = brent.drop(
    ["Open", "High", "Low", "Change %"],
    axis=1
).sort_values(by="Date", ascending=True, ignore_index=True)

# print(wti)
# print(brent)

>>>>>>> 040dd1ed1e77974cee5dca2946ddc7886f16b2c7
