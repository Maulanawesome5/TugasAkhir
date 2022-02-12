import os
from numpy import datetime_data
import pandas as pd

alamat_data = r'D:/LATIHAN PEMROGRAMAN/(TUGAS AKHIR)/Preprocess Logam dan Minyak/csv_format'
files = os.listdir(alamat_data)

try:    
    for file in files:
        if file.endswith('.csv'):
            # df = pd.read_csv(alamat_data, delimiter=';')
            df = pd.read_csv(os.path.join(alamat_data, file))

except:
    pass

print(files) # hasilnya >> ['WTI_USD.csv', 'XBR_USD.csv']

wti_data = files[0] # tipe data str
brent_data = files[1]

data1 = pd.read_csv((alamat_data + "/" + wti_data), delimiter=";")
data2 = pd.read_csv((alamat_data + "/" + brent_data), delimiter=";")
# print(data1, "\n", data2)

# Mengambil harga closing saja dari kedua dataframe
data1 = pd.DataFrame(data1).drop(['Open', 'High', 'Low', 'Change %'], axis=1)
data2 = pd.DataFrame(data2).drop(['Open', 'High', 'Low', 'Change %'], axis=1)

# Menambahkan prefix agar bisa di join antar dataframe
data1 = pd.DataFrame(data1).add_prefix('WTI_')
data2 = pd.DataFrame(data2).add_prefix('XBR_')

# Joining kedua dataframe
df = pd.DataFrame(data1).join(data2).sort_values(by=['WTI_Date', 'XBR_Date'], ascending=True, ignore_index=True)
print(df)

# Mengecek nilai yang kosong atau NaN pada data
print(df.isnull().sum()) # XBR_Date (544 NaN), XBR_Price (544 NaN) 

# Coba menyimpan dataframe menjadi file excel
saveToExcel = pd.ExcelWriter(
    r'D:/LATIHAN PEMROGRAMAN/(TUGAS AKHIR)/src/dataframe_to_excel/dummy.xlsx',
    engine="openpyxl",
    date_format="YYYY-MM-DD"
)
df.to_excel(saveToExcel, sheet_name="Crude Oil", index=False)
saveToExcel.close()

