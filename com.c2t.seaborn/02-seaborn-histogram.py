import seaborn as sns
import matplotlib.pyplot as plt

#http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.head.html#pandas.DataFrame.head
tips = sns.load_dataset('tips')
print('type(tips)=',type(tips))
df = tips.head()
print('type(df)',type(df))

print('----------------------')
print(tips)
print('----------------------')
print(df)

#Univariate plot. Just one variable.

#KDE - kernel density estimation
sns.distplot(tips['total_bill'],kde=True)
plt.show()



