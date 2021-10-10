import pandas as pd
# Create dataframe
data = {'Company':['GOOG','GOOG','MSFT','MSFT','FB','FB'],'Person':['Sam','Charlie','Amy','Vanessa','Carl','Sarah'],'Sales':[200,120,340,124,243,350]}

df = pd.DataFrame(data)
print('----------------df---------------')
print(df)

df_group_by = df.groupby('Company')
print('----------------df_group_by---------------')
print(df_group_by)

print('----------------mean---------------')
print(df_group_by.mean())

print('----------------sum---------------')
print(df_group_by.sum())

print('----------------max---------------')
print(df_group_by.max())

print('----------------describe---------------')
print(df_group_by.describe())

print('----------------transpose---------------')
print(df_group_by.describe().transpose())