import pandas as pd


df = pd.read_csv(
    'cleaned_Online_Ret.csv',
    encoding='cp1252',
    low_memory=False
)

print("Rows:", df.shape[0])
print("Columns:", df.shape[1])
print("Total Rows: ", len(df))
(df.head())

df.info()

# print(df.isna().sum())

# print(df.shape)
# print((df.head()))
# df.info()

df["Description"] = df["Description"].fillna("Unknown")
print("Missing Description values:", df["Description"].isna().sum())


df= df.astype({'Invoice':'str',
               'StockCode': 'str',
               'Description': 'str',
               'InvoiceDate': 'date64[pyarrow]',
               'CustomerID':'str',
               'Country':"str",
               'Return/Sale':'str',
               'Invoise_Status':'str',
               })
 
print("Columns:", df.shape[1])
print("Total Rows: ", len(df))
(df.head())
df.info()


print("All dublicates",df.duplicated().sum())
print("Total Rows: ", len(df))
# print("All dublicates",df[df.duplicated(subset=['Invoice'], keep=False)])
print("Total Rows: ", len(df))
df=df.drop_duplicates()
print("Total Rows: ", len(df))

print("All dublicates",df.duplicated().sum())
print("Total Rows: ", len(df))
# print(df[df.duplicated(subset=['Invoice'], keep=False)])


# print(pd.set_option('display.max_columns', None))

# print(pd.set_option('display.max_rows', 100))
print("Total Rows: ", len(df))