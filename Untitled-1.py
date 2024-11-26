# %%
import pandas as pd
import numpy as nb
import matplotlib.pyplot as plt
import seaborn as sns

# %%
df = pd.read_csv('F:\data analysis\Python_Diwali_Sales_Analysis\Python_Diwali_Sales_Analysis\Diwali Sales Data.csv',encoding= 'unicode_escape')

df

# %%
df.head()

# %%
df.shape

# %%
df.info()

# %%
df.drop(['Status','unnamed1'],axis=1,inplace=True)

# %%
pd.isnull(df)

# %%
pd.isnull(df).sum()

# %%
df.dropna(inplace=True)

# %%
df.shape

# %%
df['Amount'] = df['Amount'].astype('int')

# %%
df.info()

# %%
df.columns

# %%
df.rename(columns={'Marital_Status': 'Shaadi' })

# %%
df.describe()

# %%
ax =sns.countplot(x ='Gender',data=df)

for bars in ax.containers:
    ax.bar_label(bars)

# %%
df.groupby(['Gender'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending =False)

# %%
ax = sns.countplot(data=df,x='Age Group',hue='Gender')

# %%
sns.countplot(data=df,x='Age Group')

# %%
sales_state = df.groupby(['State'],as_index=False)['Orders'].sum().sort_values(by ='Orders',ascending=False).head(10)

# %%
sns.set(rc={'figure.figsize':(15,5)})

# %%
sns.barplot(data=sales_state,x= 'State',y='Orders')

# %%
sales_state = df.groupby(['State'],as_index=False)['Amount'].sum().sort_values(by ='Amount',ascending=False).head(10)

# %%
sns.set(rc={'figure.figsize':(15,5)})

# %%
sns.barplot(data=sales_state,x= 'State',y='Amount')

# %%
ax = sns.countplot(data=df,x='Marital_Status')

# %%
sales_state = df.groupby(['Marital_Status', 'Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.set(rc={'figure.figsize':(6,5)})
sns.barplot(data = sales_state, x = 'Marital_Status',y= 'Amount', hue='Gender')

# %%
sns.set(rc={'figure.figsize':(20,5)})
ax = sns.countplot(data=df,x='Occupation')

# %%
sales_state =df.groupby(['Occupation'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)
sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data= sales_state,x='Occupation',y='Amount')

# %%
fig1, ax1 = plt.subplots(figsize=(12,7))
df.groupby('Product_ID')['Orders'].sum().nlargest(10).sort_values(ascending=False).plot(kind='bar')
# %%



