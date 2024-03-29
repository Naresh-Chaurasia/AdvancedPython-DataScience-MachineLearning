import pandas as pd

left = pd.DataFrame({'key': ['K3', 'K1', 'K2', 'K0'],
                     'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3']})

right = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                      'C': ['C0', 'C1', 'C2', 'C3'],
                      'D': ['D0', 'D1', 'D2', 'D3']})
print(left)
print('-------------')
print(right)
print('-------------')

df_merge = pd.merge(left, right, on='key')
print(df_merge)

