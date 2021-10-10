import pandas as pd

df = pd.read_html('Table1.html')

print(df[0])