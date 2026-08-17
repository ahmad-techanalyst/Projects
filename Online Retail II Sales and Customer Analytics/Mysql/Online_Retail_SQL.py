import pandas as pd
from sqlalchemy import create_engine
import mysql.connector
import matplotlib.pyplot as plt
import seaborn as sns 

# For better charts
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12,6)


con = mysql.connector.connect(

    host='localhost',
    user= 'root',
    password='root',
    database='intern'
)

cursor = con.cursor()

df = pd.read_csv('Online_Retail_Clean.csv')

engine = create_engine ('mysql+mysqlconnector://root:root@localhost/intern')

table_name = 'Online_Retail_Cleaned.csv'

df.to_sql(
    name=table_name,
    con=engine,
    if_exists='replace',
    index=False,
    chunksize=1000
)
print("Completed")


# Revenue bby Country

query_country = """ 
SELECT
    Country,
    SUM(Quantity * Price) AS TotalRevenue From online_Retail_Clean
    GROUP BY Country
    ORDER BY TotalRevenue DESC;

"""

df_country = pd.read_sql(query_country, engine)
print('\nTop 10 country')
print(df_country.head(10))

# Top 10 country
#            Country  TotalRevenue
# 0  United Kingdom   2803731.096
# 1            EIRE     91709.710
# 2          France     59203.490
# 3         Germany     54143.460
# 4     Netherlands     41899.410
# 5          Norway     37734.170
# 6       Hong Kong     20440.630
# 7           Spain     20308.570
# 8          Sweden     17432.710
# 9       Australia     15459.920



# Revenue By Month
query_month = """ 
SELECT
    InvoiceMonth,
    SUM(Quantity * Price) AS TotalRevenue From online_Retail_Clean
    GROUP BY InvoiceMonth
    ORDER BY InvoiceMonth;
"""
df_month = pd.read_sql(query_month, engine)
print('\nRevenue by Month')
print(df_month.head(12))
# Revenue by Month
#     InvoiceMonth  TotalRevenue
# 0              1    343497.522
# 1              2    131092.536
# 2              3    266754.491
# 3              4    130856.422
# 4              5    204532.090
# 5              6    324615.610
# 6              7    155513.191
# 7              8    178479.490
# 8              9    295117.542
# 9             10    320005.360
# 10            11    286389.352
# 11            12    640259.400







query_year = """ 
SELECT
    InvoiceYear,
    SUM(Quantity * Price) AS TotalRevenue From online_Retail_Clean
    GROUP BY InvoiceYear
    ORDER BY InvoiceYear;
"""
df_year = pd.read_sql(query_year, engine)
print('\nRevenue by Year')
print(df_year.head())

# Revenue by Year
# 0         2009     83036.810
# 1         2010   1432549.293
# 2         2011   1761526.903



query_CustomerID = """ 
SELECT
    CustomerID,
    SUM(Quantity * Price) AS TotalSpend From online_Retail_Clean
    GROUP BY  CustomerID
    LIMIT 5;
"""
df_CustomerID = pd.read_sql(query_CustomerID, engine)
print('\nTotalSpend by top 5 customerID')
print(df_CustomerID.head())
# TotalSpend by top 5 customerID
# 0      Guest   436998.38
# 1      14096     8262.87
# 2      16805       20.67
# 3      16928      389.19
# 4      17539      202.75


query_Product = """ 
SELECT
    Description,
    SUM(Quantity * Price) AS TotalRevenue
    FROM online_Retail_Clean
    WHERE Description IS NOT NULL
    GROUP BY  Description
    ORDER BY TotalRevenue DESC
    LIMIT 10;
"""
df_Product = pd.read_sql(query_Product, engine)
print('\nTop 10 Products')
print(df_Product.head(10))

# Top 10 Products
#                           Description  TotalRevenue
# 0                              Manual     718709.87
# 1         PAPER CRAFT , LITTLE BIRDIE     336939.20
# 2                          AMAZON FEE     262456.10
# 3      MEDIUM CERAMIC TOP STORAGE JAR     154429.62
# 4            REGENCY CAKESTAND 3 TIER      74025.53
# 5                             POSTAGE      55626.01
# 6      PICNIC BASKET WICKER 60 PIECES      39619.50
# 7                        Bank Charges      32540.06
# 8  WHITE HANGING HEART T-LIGHT HOLDER      32456.89
# 9                       CHILLI LIGHTS      24337.93



