SELECT * FROM intern.`online_ret.csv`;


SELECT
    Country,
    SUM(Quantity * Price) AS TotalRevenue From online_Retail_Clean
    GROUP BY Country
    ORDER BY TotalRevenue DESC;
    
    
    
SELECT
    InvoiceMonth,
    SUM(Quantity * Price) AS TotalRevenue From online_Retail_Clean
    GROUP BY InvoiceMonth
    ORDER BY InvoiceMonth;
    
    
SELECT
    InvoiceYear,
    SUM(Quantity * Price) AS TotalRevenue From online_Retail_Clean
    GROUP BY InvoiceYear
    ORDER BY InvoiceYear;
    
    
SELECT
    CustomerID,
    SUM(Quantity * Price) AS TotalSpend From online_Retail_Clean
    GROUP BY  CustomerID
    LIMIT 5;
    
    
SELECT
    Description,
    SUM(Quantity * Price) AS TotalRevenue
    FROM online_Retail_Clean
    WHERE Description IS NOT NULL
    GROUP BY  Description
    ORDER BY TotalRevenue DESC
    LIMIT 10;
    
    
