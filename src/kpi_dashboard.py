class ExecutiveDashboard:

    def __init__(self,df,rfm_table):
        self.df = df
        self.rfm_table = rfm_table

    # 1. Total revenue
    def total_revenue(self):
        return self.df['Revenue'].sum() # returns the total revenue generated so far

    # 2. Total Customers
    def total_customers(self):
        return self.df['CustomerID'].nunique() # returns the unique customers

    # 3. Total orders
    def total_orders(self):
        return self.df['InvoiceNo'].nunique() # returns total number of unique invoice generated
    
    # 4. Average order value (AOV)
    def average_order_value(self):
        revenue = (
            self.total_revenue()
        )

        orders = (
            self.total_orders()
        )

        return revenue / orders
    
    # 5. Top Country
    def top_country(self):
        return (
            self.df.groupby(
                'Country'
            )['Revenue']
            .sum()
            .idxmax()
        )

    # 6. Top Product
    def top_product(self):
        return (
            self.df.groupby(
                'Description'
            )['Revenue']
            .sum()
            .idxmax()
        )
    
    # 7. VIP customers
    def vip_customers(self):
        return (
            self.rfm_table[
                self.rfm_table[
                    'Segment'
                ] == 'VIP Customer'
            ]
            .shape[0]
        )

    # Generating dashboard
    def generate_dashboard(self):
        print(
            "\n" + "=" * 50
        )

        print(
            "EXECUTIVE KPI DASHBOARD"
        )

        print(
            "=" * 50
        )

        print(
            f"Total Revenue: "
            f"{self.total_revenue():,.2f}"
        )

        print(
            f"Total Customers: "
            f"{self.total_customers()}"
        )

        print(
            f"Total Orders: "
            f"{self.total_orders()}"
        )

        print(
            f"Average Order Value: "
            f"{self.average_order_value():.2f}"
        )

        print(
            f"Top Country: "
            f"{self.top_country()}"
        )

        print(
            f"Top Product: "
            f"{self.top_product()}"
        )

        print(
            f"VIP Customers: "
            f"{self.vip_customers()}"
        )

        print(
            "=" * 50
        )