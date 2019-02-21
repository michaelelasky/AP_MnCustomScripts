import sys
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

file_location = r'C:\Users\elas1mik\Desktop\ASSHTO\sampl.xlsx'
'''#df = pd.read_excel('sampl.xlsx')
df = pd.read_excel(file_location)

#print the column names
print df.columns

#get the values for a given column
values = df['column_name'].values

#get a data frame with selected columns
FORMAT = ['Col_1', 'Col_2', 'Col_3']
df_selected = df[FORMAT]'''

df = pd.read_excel(file_location, sheet_name='Sheet1')
 
print("Column headings:")
print(df.columns)

for i in df.index:
	print(df['this'][i])