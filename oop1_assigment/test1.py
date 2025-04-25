import pandas as pd
import os

path = os.path.join(os.path.dirname(__file__), 'sales.xlsx')
data = pd.read_excel(path)

print(data)
total_sales = data['Total Sales'].sum()

print(f"Total sales: {total_sales}")