class FeatureEngineer:
    def __init__(self, df):
        self.df = df.copy()

    def create_revenue_column(self):
        self.df['Revenue'] = (
            self.df['Quantity'] * self.df['UnitPrice']
        )
    """
    1. Why ?
    A. profit analysis, yearly sales, monthly sales, day to day sales...
    
    """

    def extract_year(self):  # new column
        self.df['Year'] = (
            self.df['InvoiceDate']
            .dt.year
        )

    def extract_month(self):
        self.df['Month'] = (
            self.df['InvoiceDate']
            .dt.month
        )

    def extract_day(self):
        self.df['Day'] = (
            self.df['InvoiceDate']
            .dt.day
        )

    def extract_hour(self):
        self.df['Hour'] = (
            self.df['InvoiceDate']
            .dt.hour
        )

    def extract_day_name(self):
        self.df['DayName'] = (
            self.df['InvoiceDate']
            .dt.day_name()
        )

    def engineer_features(self):  # driver function
        print("\nStarting Feature Engineering...")

        self.create_revenue_column()
        self.extract_year()
        self.extract_month()
        self.extract_day()
        self.extract_hour()
        self.extract_day_name()

        print(" Feature Engineering Completed")

        return self.df