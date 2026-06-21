import pandas as pd
import os

class DataLoader:
    def __init__(self, file_path, encoding="utf-8"):
        self.file_path = file_path
        self.encoding = encoding

    def validate_file(self):
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"File not found: {self.file_path}")

    def load_data(self):
        try:
            self.validate_file()
            df = pd.read_csv(self.file_path, encoding=self.encoding)
            print("Data loaded successfully")
            return df
        except Exception as e:
            print(f" Error loading data: {e}")
            raise