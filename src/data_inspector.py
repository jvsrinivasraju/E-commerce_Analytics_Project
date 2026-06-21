# Data inspection

import pandas as pd

class DataInspector:
    def __init__(self, df):
        self.df = df

    def preview_data(self, n=5):  # blueprint
        print("\nFirst Rows:")
        print(self.df.head(n))

    def dataset_shape(self): # rows,cols
        rows, cols = self.df.shape
        print(f"\nDataset Shape: {rows} rows, {cols} columns")

    def column_info(self):
        print("\nColumn Information:")
        print(self.df.info()) # col names, datatypes, non-empty vlaues, memory used

    def column_names(self):
        print("\nColumn Names:")
        print((self.df.columns))

    def statistical_summary(self):
        print("\nStatistical Summary:")
        print(self.df.describe())