import pandas as pd
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 


df = pd.read_csv(
    'cleaned_Online_Ret.csv',
    encoding='cp1252',
    low_memory=False
)

# print("Rows:", df.shape[0])
# print("Columns:", df.shape[1])
print("Total Rows: ", len(df))
# (df.head())

# df.info()

# # print(df.isna().sum())

# # print(df.shape)
# # print((df.head()))
# # df.info()

# df["Description"] = df["Description"].fillna("Unknown")
# print("Missing Description values:", df["Description"].isna().sum())


# df= df.astype({'Invoice':'str',
#                'StockCode': 'str',
#                'Description': 'str',
#                'InvoiceDate': 'date64[pyarrow]',
#                'CustomerID':'str',
#                'Country':"str",
#                'Return/Sale':'str',
#                'Invoise_Status':'str',
#                })
 
# print("Columns:", df.shape[1])
# print("Total Rows: ", len(df))
# (df.head())
# df.info()


# print(df.duplicated().sum())
 
# df=df.drop_duplicates()
# print(df.duplicated().sum())
# print(df[df.duplicated(subset=['Invoice'], keep=False)])


# print(pd.set_option('display.max_columns', None))

# print(pd.set_option('display.max_rows', 100))
# print("Total Rows: ", len(df))

# df.to_csv('Online_Retail_Clean.csv', index=False)
# print("Success")




#############

# invc_D=df['InvoiceDate']
# print(invc_D.dtype)


# Revenue Trend Over Time Line Chart
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
# print(df['InvoiceDate'].dtype)

df['Month'] = df['InvoiceDate'].dt.to_period('M')
monthly_rev = df.groupby('Month')['Revenue'].sum().reset_index()
monthly_rev['Month'] = monthly_rev['Month'].astype(str)

plt.plot(monthly_rev['Month'], monthly_rev['Revenue'], marker='o')
plt.title("Revenue Trend Over Time")
plt.xticks(rotation=45)
plt.ylabel("Total Revenue")
plt.show()



# Top 10 country bu revenue Bar Chart
top_countries = df.groupby('Country')['Revenue'].sum().sort_values(ascending=False).head(10)

sns.barplot(x=top_countries.values, y=top_countries.index, palette='Blues_d')
plt.title("Top 10 country by revenue")
plt.xlabel("Total Revenue")
plt.show()


# Top 10  products Bar chart
top_product = df.groupby('Description')['Revenue'].sum().sort_values(ascending=False).head(10)

sns.barplot(x=top_product.values, y=top_product.index, palette='Greens_d')
plt.title("Top 10 Product by revenue")
plt.xlabel("Total Revenue")
plt.tight_layout()
plt.show()



# Average Order Value = Total Revenue / Unique Invoices 
aov= df.groupby("Country").agg(
    TotalRevenue = ("Revenue", "sum"),
    UniqueOrders = ("Invoice", "nunique")
    )

aov['AOV'] = aov ['TotalRevenue'] / aov ['UniqueOrders']
aov = aov.sort_values('AOV',ascending=False).head(15)

sns.heatmap(aov[['AOV']],annot=True, fmt='.2f',cmap='YlGnBu')
plt.title('Average Order Value by country')
plt.show()




df.to_csv('Online_Retail_Clean.csv', index=False)
print(len(df))
print("Finish")