import pandas as pd

class RFMAnalyzer:

    def __init__(self, df):
        self.df = df.copy()

    def calculate_rfm(self):

        # Reference date
        reference_date = (
            self.df['InvoiceDate'].max()  # latest date
            + pd.Timedelta(days=1)
        )

        # Create RFM table
        rfm = (
            self.df.groupby('CustomerID')
            .agg({  # you take one customer and produce a single row for each customer having only below features
                
                # 1. Recency
                'InvoiceDate': lambda x:  # higher order functions
                    (reference_date - x.max()).days,

                # 2. Frequency
                'InvoiceNo': 'nunique',

                # 3. Monetary
                'Revenue': 'sum'
            })
        )

        # Rename columns
        rfm.columns = [
            'Recency',
            'Frequency',
            'Monetary'
        ]

        return rfm
    

    def create_rfm_scores(self, rfm):

        rfm['R_Score'] = pd.qcut(
            rfm['Recency'],
            5,
            labels=[5,4,3,2,1]
        )

        rfm['F_Score'] = pd.qcut(
            rfm['Frequency'].rank(method='first'),
            5,
            labels=[1,2,3,4,5]
        )

        rfm['M_Score'] = pd.qcut(
            rfm['Monetary'],
            5,
            labels=[1,2,3,4,5]
        )

        return rfm
    
    def combine_rfm_score(self, rfm):

        rfm['RFM_Score'] = (
            rfm['R_Score'].astype(str)
            + rfm['F_Score'].astype(str)
            + rfm['M_Score'].astype(str)
        )
        # rfm.sort_values('RFM_Score')

        return rfm

    def assign_segment(self,row):
        r = int(row['R_Score'])
        f = int(row['F_Score'])
        m = int(row['M_Score'])

        if r>=4 and f>=4 and m >=4:
            return "VIP Customer"
        elif f>=4 and m>=3:
            return "Loyal Customer"
        elif r>=4:
            return "Growing Customer"
        elif r<=2 and f<=2 and m<=2:
            return "Lost Customer"
        else:
            return "Regular Customer"

    def create_segments(self, rfm):

        rfm['Segment'] = (
            rfm.apply(  # repeteadly calls the function for every row
                self.assign_segment, # function (takes 1 single entire row and pass it to the specified function)
                axis=1  # axis (row-wise)
            ) # and it expects the return value, and stores that values in rfm['Segement'] column
        )

        return rfm
    
    def segment_summary(self, rfm):
        summary_table = (
            rfm['Segment']
            .value_counts()
        )

        print("\nCustomer Segments")

        print(summary_table)

        return summary_table