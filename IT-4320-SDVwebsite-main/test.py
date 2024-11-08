import pandas as pd

csv_filepath = 'nasdaq-listed.csv'
file = pd.read_csv(csv_filepath)

symbols = file['Symbol'].tolist()

for sym in symbols:
    print(sym)
