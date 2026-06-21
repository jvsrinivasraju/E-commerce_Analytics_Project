import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

class EDAAnalyzer:
    def __init__(self, df):
        self.df = df.copy()

    # 1. Revenue analysis

    def total_revenue(self):
        revenue = self.df['Revenue'].sum()  # one value

        print("\n Total Revenue:")
        print(f"${revenue:,.2f}")

    def revenue_distribution(self):
        plt.figure(figsize=(10, 6))
        mydf = self.df[ (self.df['Revenue']<10000) & (self.df['Revenue']>10)]
        sns.histplot(
            mydf['Revenue'],
            bins=50,
            kde=True
        )

        plt.title("Revenue Distribution")
        plt.xlabel("Revenue")
        plt.ylabel("Frequency")

        plt.show()

        """
        Interpretations:
            --> one small bar and one large bar
            --> huge small transactions and few huge transactions
            --> its a highly Right Skewed distribution
            --> target customers : middle class, and lower middle class people
            --> too much ambience : Not preffered
        """

    # 2. Product analysis
    def top_products_by_quantity(self):

        # top_products --> variable/container
        top_products = (  
            self.df.groupby('Description')['Quantity']
            .sum()
            .sort_values(ascending=False)
            .head(10)
        ) # small brackets are used for writing your code in multiple lines

        print("\nTop Products by Quantity:")
        print(top_products)

        plt.figure(figsize=(12,6))  # 1 unit = 1 inch (2.54 cm) (bydefualt matplotlib)

        top_products.plot(kind='bar')

        plt.title("Top 10 Products by Quantity Sold")
        plt.xlabel("Product")
        plt.ylabel("Quantity Sold")

        plt.xticks(rotation=90)

        plt.show()

        """
        Insights : 
            1. High Demand products : DESIGNS, ROSPOT
        
        """

    def top_products_by_revenue(self):

        top_revenue = (
            self.df.groupby('Description')['Revenue']
            .sum()
            .sort_values(ascending=False)
            .head(10)
        )

        print("\nTop Products by Revenue:")
        print(top_revenue)

        plt.figure(figsize=(12,6))

        top_revenue.plot(kind='bar')

        plt.title("Top 10 Products by Revenue")
        plt.xlabel("Product")
        plt.ylabel("Revenue")

        plt.xticks(rotation=90)

        plt.show()


    def product_purchase_frequency(self):

        frequency = (
            self.df['Description']
            .value_counts()  # inbuilt : counts the occurences
            .head(10)
        )

        print("\nProduct Purchase Frequency:")
        print(frequency)

        plt.figure(figsize=(12,6))

        sns.barplot(
            x=frequency.values,  # occurences  (values)
            y=frequency.index  # Description (names)
        )

        plt.title("Product Purchase Frequency")

        plt.xlabel("Frequency")
        plt.ylabel("Product")

        plt.show()


    # 3. Customer Analysis

    def top_customers_by_revenue(self):

        top_customers = (
            self.df.groupby('CustomerID')['Revenue']
            .sum()
            .sort_values(ascending=False)
            .head(10)
        )

        print("\n Top Customers By Revenue:")
        print(top_customers)

        plt.figure(figsize=(12,6))

        sns.barplot(
            x=top_customers.index,
            y=top_customers.values
        )

        plt.title("Top 10 Customers By Revenue")

        plt.xlabel("Customer ID")
        plt.ylabel("Revenue")

        plt.xticks(rotation=45)

        plt.show()


    def purchase_frequency(self):

        frequency = (
            self.df['CustomerID']
            .value_counts()
            .head(10)
        )

        print("\n Customer Purchase Frequency:")
        print(frequency)

        plt.figure(figsize=(12,6))

        sns.barplot(
            x=frequency.index,
            y=frequency.values
        )

        plt.title("Top Customers By Purchase Frequency")

        plt.xlabel("Customer ID")
        plt.ylabel("Number of Purchases")

        plt.xticks(rotation=45)

        plt.show()


    def customer_revenue_distribution(self):

        customer_revenue = (
            self.df.groupby('CustomerID')['Revenue']
            .sum()
        )
        print(customer_revenue) # not a single number

        plt.figure(figsize=(12,6))

        sns.histplot(
            customer_revenue,
            bins=50,
            kde=True
        )

        plt.title("Customer Revenue Distribution")

        plt.xlabel("Revenue")

        plt.show()    


    # 4. Country-wise Analysis

    def revenue_by_country(self):

        country_revenue = (
            self.df.groupby('Country')['Revenue']
            .sum()
            .sort_values(ascending=False)
            .head(10)
        )

        print("\n Revenue By Country:")
        print(country_revenue)

        plt.figure(figsize=(12,6))

        sns.barplot(
            x=country_revenue.values,
            y=country_revenue.index
        )

        plt.title("Top 10 Countries By Revenue")
        plt.xlabel("Revenue")
        plt.ylabel("Country")

        plt.show()


    def customers_by_country(self):

        customer_count = (
            self.df.groupby('Country')['CustomerID']
            .nunique() # returns count and deletes no one
            .sort_values(ascending=False)
            .head(10)
        )

        print("\n Customers By Country:")
        print(customer_count)

        plt.figure(figsize=(12,6))

        sns.barplot(
            x=customer_count.values,
            y=customer_count.index
        )

        plt.title("Top 10 Countries By Customer Count")

        plt.xlabel("Customers")
        plt.ylabel("Country")

        plt.show()


    def transactions_by_country(self):

        transaction_count = (
            self.df['Country']
            .value_counts()
            .head(10)
        )

        print("\n Transactions By Country:")
        print(transaction_count)

        plt.figure(figsize=(12,6))

        sns.barplot(
            x=transaction_count.values,
            y=transaction_count.index
        )

        plt.title("Top 10 Countries By Transactions")

        plt.xlabel("Transactions")
        plt.ylabel("Country")

        plt.show()

    # 5. Time-based Analysis

    def monthly_revenue_trend(self):

        monthly_sales = (
            self.df.groupby('Month')['Revenue']
            .sum()
        )

        plt.figure(figsize=(12,6))

        sns.lineplot(
            x=monthly_sales.index,
            y=monthly_sales.values,
            marker='o'
        )

        plt.title("Monthly Revenue Trend")

        plt.xlabel("Month")
        plt.ylabel("Revenue")
        plt.xticks(
            ticks=range(1,13),
            labels = ['jan','feb','mar','apr','may','jun','july','aug','sept','oct','nov','dec']
        )

        plt.show()


    def hourly_purchase_pattern(self):

        hourly_data = (
            self.df.groupby('Hour')['InvoiceNo']
            .count()
        )

        plt.figure(figsize=(12,6))

        sns.lineplot(
            x=hourly_data.index,
            y=hourly_data.values,
            marker='o'
        )

        plt.title("Hourly Purchase Pattern")

        plt.xlabel("Hour")
        plt.ylabel("Transactions")

        plt.show()


    def weekday_analysis(self):

        weekday_sales = (
            self.df.groupby('DayName')['Revenue']
            .sum()
        )

        order = [
                'Monday',
                'Tuesday',
                'Wednesday',
                'Thursday',
                'Friday',
                'Saturday',
                'Sunday'
            ]

        weekday_sales = weekday_sales.reindex(order)  # re-ordering of data

        plt.figure(figsize=(12,6))

        sns.barplot(
            x=weekday_sales.index,
            y=weekday_sales.values
        )

        plt.title("Weekday Revenue Analysis")

        plt.xlabel("Day")
        plt.ylabel("Revenue")

        plt.xticks(rotation=45)

        plt.show()



    # 6. Statistical Distribution and Correlation Analysis
    
    def revenue_statistics(self):

        revenue = self.df['Revenue']

        print("\n Revenue Statistics")

        print(f"Mean: {revenue.mean():.2f}")   # average revenue
        print(f"Median: {revenue.median():.2f}") # middle revenue value : easy to find outliners
        print(f"Standard Deviation: {revenue.std():.2f}") # spread
        # low std --> no such noticable variation in revenue
        # high std --> revenue varies greatly...
        print(f"Minimum: {revenue.min():.2f}") # lowest revenue
        print(f"Maximum: {revenue.max():.2f}") # highest revenue


    def revenue_boxplot(self):

        plt.figure(figsize=(10,6))

        sns.boxplot(
            x=self.df['Revenue']  # horizontal
        )

        plt.title("Revenue Boxplot")

        plt.show()

    """
        -> boxplot is collapsed because of outliners
        -> your vertical line in the graph itself is the boxplot
    
    """
    def correlation_analysis(self):
        # co-relation analysis is only only only based on numericals columns
        numeric_df = self.df.select_dtypes(
            include=np.number  # inlucdes both int and floating point numbers
        )

        correlation = numeric_df.corr()  # mathematical : pearson corelation

        plt.figure(figsize=(12,8))

        sns.heatmap(  # graph : visualization part # heatmap : nothing but colored matrix
            correlation,
            annot=True,
            cmap='coolwarm'
            
              #  -ve : blue color schema
              #    0 : no/light color
              #  +ve : red color schema
        )

        plt.title("Correlation Heatmap")

        plt.show()


    def skewness_analysis(self):  # imp in ML 
        # how assymetric your distribution...

        skewness = self.df['Revenue'].skew()
        
        print("\n Revenue Skewness")
        print(f"Skewness: {skewness:.2f}")

        if skewness > 0:
            print("Right Skewed Distribution")

        elif skewness < 0:
            print("Left Skewed Distribution")

        else:
            print("Approximately Symmetric")   # mean ~ median