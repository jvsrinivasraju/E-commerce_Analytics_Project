class DataQualityAnalyzer:
    def __init__(self, df):
        self.df = df

    def check_missing_values(self):
        print("\nMissing Values:")
        missing = self.df.isnull().sum()
        print(missing[missing > 0])

    def check_duplicates(self):
        print("\nDuplicate Records:")
        duplicates = self.df.duplicated().sum()
        print(f"Total Duplicate Rows: {duplicates}")

    def check_negative_quantities(self):
        print("\nNegative Quantity Records:")
        negative_qty = self.df[self.df['Quantity'] < 0]
        print(f"Total Negative Quantity Rows: {len(negative_qty)}")
        # negetive quatitty may represent the returns

    def check_zero_or_negative_prices(self):
        print("\nInvalid Unit Prices:")
        invalid_prices = self.df[self.df['UnitPrice'] <= 0]
        print(f"Total Invalid Price Rows: {len(invalid_prices)}")

    def check_unique_countries(self):
        print("\nUnique Countries:")
        print(self.df['Country'].unique()) # prints each country one single time

    def generate_quality_summary(self):  # driver function
        print("\nDATA QUALITY SUMMARY")
        print("-" * 40)

        # calling functions...
        self.check_missing_values()
        self.check_duplicates()
        self.check_negative_quantities()
        self.check_zero_or_negative_prices()
        self.check_unique_countries()