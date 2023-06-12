wb = xw.Book('./data.csv')
sht1 = wb.sheets[0]
ct = sht1.range('A1').options(pd.DataFrame, index=False, header=True, expand='table').value
# ct = ct.set_index(None, inplace=True)
print(ct)
