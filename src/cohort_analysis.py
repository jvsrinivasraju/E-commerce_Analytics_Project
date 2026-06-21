import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class CohortAnalyzer:
    def __init__(self,df): # constructor
        self.df = df.copy()

    # 1. From invoice date to purchase month
    def create_purchase_month(self):
        self.df['PurchaseMonth'] = (
            self.df['InvoiceDate']
            .dt.to_period('M') # 2011-01
        )
        return self.df
    
    # 2. cohort month
    def create_cohort_month(self):
        self.df['CohortMonth'] = (
            self.df.groupby('CustomerID') # group all records belong to same customer
            ['PurchaseMonth']
            .transform('min')
        )

        return self.df

    # 3. cohort index
    def create_cohort_index(self):
        purchase_year = (
            self.df['PurchaseMonth']
            .dt.year
        )

        purchase_month = (
            self.df['PurchaseMonth']
            .dt.month
        )

        cohort_year = (
            self.df['CohortMonth']
            .dt.year
        )

        cohort_month = (
            self.df['CohortMonth']
            .dt.month
        )

        self.df['CohortIndex'] = (
            (purchase_year - cohort_year) * 12
            +
            (purchase_month - cohort_month)
        )

        return self.df

    # 4. cohort matrix
    def create_cohort_matrix(self):
        cohort_data = (  # cohort_data is just a variable/container
            self.df.groupby(
                [
                    'CohortMonth',
                    'CohortIndex'
                ]
            )['CustomerID']
            .nunique()
            .reset_index() # avoids multi indexing (dont allow empty columns)
        )

        cohort_matrix = (
            cohort_data.pivot(
                index='CohortMonth',  # rows
                columns='CohortIndex', # cols
                values='CustomerID'  # respective values
            )
        )

        return cohort_matrix



    def create_retention_matrix(self,cohort_matrix):
        retention_matrix = (
            cohort_matrix.divide(
                cohort_matrix.iloc[:, 0], # : --> consider all rows , 0 --> consider only 0th column
                axis=0 # you plz do the operations row by row
            )
            * 100
        )

        return retention_matrix


    # 5. Heatmaps
    def plot_retention_heatmap(self,retention_matrix):
        plt.figure(
            figsize=(14,8)
        )

        sns.heatmap(  # sns is a seaborn Alias
            retention_matrix,
            annot=True,  # you will see the values inside the boxes
            fmt=".1f",  # values will be rounded off to .1 decimal places
            cmap="Blues" # color Schema
        )

        plt.title(
            "Customer Retention Heatmap (%)"
        )

        plt.xlabel(
            "Cohort Index"
        )

        plt.ylabel(
            "Cohort Month"
        )

        plt.show()