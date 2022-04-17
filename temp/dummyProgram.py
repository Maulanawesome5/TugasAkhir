import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from minyak import brent, wti

# path directory
# dataset = r'D:\LATIHAN PEMROGRAMAN\(TUGAS AKHIR)\XBR_USD Historical Data.csv' # format tanggal menyebalkan
alamat_data = r'D:/LATIHAN PEMROGRAMAN/(TUGAS AKHIR)/Preprocess Logam dan Minyak/csv_format/Brent Oil Futures Historical Data.csv'


# membuat dataframe
df = pd.read_csv(alamat_data, delimiter=";") # 1329 baris, 7 kolom
df

# drop kolom, mengambil kolom tanggal dan price
brent_futures = pd.DataFrame(df).drop(['Open', 'High', 'Low', 'Vol.', 'Change %'], axis=1).add_prefix('BRENT_')
brent_usd = pd.DataFrame(brent).drop(['Date', 'Open', 'High', 'Low', 'Change %'], axis=1).add_prefix('XBR_')
wti_usd = pd.DataFrame(wti).drop(['Date', 'Open', 'High', 'Low', 'Change %'],axis=1).add_prefix('WTI_')

brent_futures # 1329 baris
wti_usd # 1532 baris

# join dua dataframe
oilPrice = pd.DataFrame(brent_futures).join(wti_usd).sort_values(by=['BRENT_Date'], ascending=True, ignore_index=True)
# print(oilPrice, f"\n{oilPrice.isnull().sum()}") # 0 nilai null

# mencari logaritma persentase perubahan
xbr = oilPrice['BRENT_Price'].pct_change().apply(lambda x: np.log(1+x))
westTexas = oilPrice['WTI_Price'].pct_change().apply(lambda x: np.log(1+x))

# menghitung varians
var_xbr = xbr.var() # 0.0006971281387836002
var_wti = westTexas.var() # 0.0009527147425308298

# mengukur volatilitas
xbr_vol = np.sqrt(var_xbr * 250) # 0.41747099862852755
wti_vol = np.sqrt(var_wti * 250) # 0.4880355372641499



