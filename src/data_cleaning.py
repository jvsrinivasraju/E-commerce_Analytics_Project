import pandas as pd

class DataCleaner:
    def __init__(self, df):
        self.df = df.copy()  # it creates a duplicate copy of df

    def remove_missing_customer_ids(self): # removing the rows where customer id is missing
        self.df = self.df.dropna(subset=['CustomerID'])  # subset=['CustomerID']  --> only checks the customer_id column

    def remove_duplicates(self): # removes the duplicate rows
        self.df = self.df.drop_duplicates()

    def remove_invalid_prices(self):  # neglecting negative prices
        self.df = self.df[self.df['UnitPrice'] > 0] # boolean filtering

    def convert_invoice_date(self):
        self.df['InvoiceDate'] = pd.to_datetime( # impose timestamp to your invoice date
            self.df['InvoiceDate']
        )

    def convert_customer_id(self):
        self.df['CustomerID'] = (
            self.df['CustomerID']
            .astype(int) # converts if any doubles to pure ints
            .astype(str) # then convert it into a string
        )

    def standardize_descriptions(self):
        self.df['Description'] = (
            self.df['Description']
            .str.strip() # removes unneccesary spaces (leading and trailing)
            .str.upper() # entire product description will be converted to upper case (uniform data(either lowercase or uppercase is preferred))
        )

    def clean_data(self):  # driver function
        print("\nStarting Data Cleaning...")

        self.remove_missing_customer_ids()
        self.remove_duplicates()
        self.remove_invalid_prices()
        self.convert_invoice_date()
        self.convert_customer_id()
        self.standardize_descriptions()

        print("Data Cleaning Completed")

        return self.df