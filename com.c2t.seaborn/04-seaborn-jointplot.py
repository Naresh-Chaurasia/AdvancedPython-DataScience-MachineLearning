import seaborn as sns
import matplotlib.pyplot as plt

#https://seaborn.pydata.org/generated/seaborn.jointplot.html#seaborn.jointplot
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
sns.jointplot(x="total_bill", y="tip", data=tips)
plt.show()



