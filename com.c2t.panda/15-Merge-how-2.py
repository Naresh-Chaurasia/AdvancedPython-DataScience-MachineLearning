import pandas as pd

left = pd.DataFrame({'key1': ['K0', 'K1', 'K2', 'K4'],
                     'key2': ['K0', 'K1', 'K0', 'K1'],
                     'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3']})

right = pd.DataFrame({'key1': ['K0', 'K1', 'K2', 'K3'],
                      'key2': ['K0', 'K0', 'K0', 'K0'],
                      'C': ['C0', 'C1', 'C2', 'C3'],
                      'D': ['D0', 'D1', 'D2', 'D3']})

print(left)
print('---------------')
print(right)
print('---------------')
left_merge = pd.merge(left, right, how='left', on='key1')
print(left_merge)