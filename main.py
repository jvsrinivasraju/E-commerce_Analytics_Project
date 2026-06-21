from src.data_loader import DataLoader  # from a particular file, import a particular class
from src.data_inspector import DataInspector
from src.data_quality import DataQualityAnalyzer
from src.data_cleaning import DataCleaner
from src.feature_engineering import FeatureEngineer
from src.eda import EDAAnalyzer
from src.rfm_analysis import RFMAnalyzer
from src.cohort_analysis import CohortAnalyzer
from src.kpi_dashboard import ExecutiveDashboard

import config  # importing a file

def main():
    # 1. data loading phase
    loader = DataLoader(config.DATA_PATH, config.ENCODING)
    df = loader.load_data()

    # 2. data inspection phase
    inspector = DataInspector(df)  # we are introducing our data frame to the datainspector class

    inspector.preview_data()
    inspector.dataset_shape()
    inspector.column_info()
    inspector.column_names()
    inspector.statistical_summary()

    # 3. Quality check
    quality_check = DataQualityAnalyzer(df)
    quality_check.generate_quality_summary()

    # 4. Cleaning the data
    data_cleaner = DataCleaner(df)
    cleaned_df = data_cleaner.clean_data()

    # 5. Feature Engineering
    engineer = FeatureEngineer(cleaned_df)
    featured_df = engineer.engineer_features()

    print("\nFeatured Data Frame")
    print(featured_df.head(10))

    print(featured_df.columns)

    # 6. EDA
    eda_obj = EDAAnalyzer(featured_df)  # object creation

    # (i) Revenue Analysis
    # eda_obj.total_revenue()
    # eda_obj.revenue_distribution()

    # # (ii) Product Analysis
    # eda_obj.top_products_by_quantity()  # which products are sold in highest quantity
    # eda_obj.top_products_by_revenue()  # which products generated the highest revenue
    # eda_obj.product_purchase_frequency()  # how many times a particular product is purchased (most/least)

    # (iii) Customer Analysis
    # eda_obj.top_customers_by_revenue()
    # eda_obj.purchase_frequency()
    # eda_obj.customer_revenue_distribution()

    # (iv) Country-wise Analysis
    # eda_obj.revenue_by_country()
    # eda_obj.customers_by_country()
    # eda_obj.transactions_by_country()

    # # (v) Time-based Analysis
    # eda_obj.monthly_revenue_trend()
    # eda_obj.hourly_purchase_pattern()
    # eda_obj.weekday_analysis()

    # # (vi) Statistical Distribution and Correlation Analysis
    # eda_obj.revenue_statistics()
    # eda_obj.revenue_boxplot()
    # eda_obj.correlation_analysis()
    # eda_obj.skewness_analysis()





    # *** Adv Analytics ***

    # 1. RFM Analysis
    rfm_analyzer = RFMAnalyzer(featured_df)
    rfm_table = rfm_analyzer.calculate_rfm()

    rfm_table = rfm_analyzer.create_rfm_scores(rfm_table)

    rfm_table = rfm_analyzer.combine_rfm_score(rfm_table)
    print(rfm_table.head())


    rfm_table = rfm_analyzer.create_segments(rfm_table)

    print(rfm_table[['RFM_Score','Segment']].head())

    rfm_analyzer.segment_summary(rfm_table)


    # Cohort Analysis

    cohort = CohortAnalyzer(featured_df)

    temp_df = cohort.create_purchase_month()

    print(temp_df[['InvoiceDate','PurchaseMonth']].head(10))

    temp_df = cohort.create_cohort_month()

    print(temp_df[['InvoiceDate','PurchaseMonth','CohortMonth']].head(10))

    temp_df = cohort.create_cohort_index()

    print(
        temp_df[
            [
                'CustomerID',
                'PurchaseMonth',
                'CohortMonth',
                'CohortIndex'
            ]
        ]
        .sample(200) # random 200 rows will be generated
    )

    cohort_matrix = (
    cohort.create_cohort_matrix()
    )

    print("\nCOHORT MATRIX")

    print(cohort_matrix.head())

    retention_matrix = cohort.create_retention_matrix(cohort_matrix)
    print(retention_matrix.round(2))

    # Heatmap
    cohort.plot_retention_heatmap(retention_matrix)


    # KPI dashboard
    dashboard = ExecutiveDashboard(featured_df,rfm_table)
    dashboard.generate_dashboard()

if __name__ == "__main__":
    main()