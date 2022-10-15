import tabula as tb
import pandas as pd
import re


pdf_file = './assets/liberia_pdf.pdf'
data = tb.read_pdf(pdf_file, area = (100, 0, 600, 800), pages=3)

df = pd.DataFrame(data[0])

#remove unwanted columns
df.drop(df.columns[[1,2,3,4,5,6,7,8]], axis=1, inplace=True)

df.columns = ['County', 'Cummulative Deaths']
df.to_csv('downloads/liberia_pdf.csv', index=False)