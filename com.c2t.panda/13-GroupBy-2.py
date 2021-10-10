import pandas as pd
# Create dataframe
data = {'Company':['GOOG','GOOG','MSFT','MSFT','FB','FB'],
        'Person':['Sam','Charlie','Amy','Vanessa','Carl','Sarah'],
        'Sales':[200,120,340,124,243,350]}

df = pd.DataFrame(data)
print(df)

df_gp = df.groupby('Company')
print('----Company----')
print(df_gp)

df_gp_mean = df_gp.mean()
print('--------------')
print(df_gp_mean)

df_gp_sum = df_gp.sum()
print('--------------')
print(df_gp_sum)

print('------describe--------')
print(df_gp.describe().transpose())

