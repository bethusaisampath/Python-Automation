import tabula
from tabula import read_pdf

table = tabula.read_pdf('weather.pdf', pages=1)

print(type(table[0]))
#print(table)
table[0].to_csv('output.csv', index=None)