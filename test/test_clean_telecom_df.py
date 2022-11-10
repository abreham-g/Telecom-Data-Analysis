import os
import sys
import unittest
import pandas as pd
import pandas.api.types as ptypes


sys.path.append(os.path.abspath(os.path.join('..')))

from clean_telecom_df import CleanTelecomData
from helper import TelecomHelper


df = pd.read_csv("./Data/data.csv")


class TestCleanTCleanTelecomDatae(unittest.TestCase):
    
    def setUp(self):
        
        self.df = df.head(1000).copy(deep=True)
        self.df.columns = [column.replace(' ', '_').lower()
                           for column in self.df.columns]
        self.cleaner = CleanTelecomData(self.df)

        

    def test_drop_duplicate(self):
        df = self.cleaner.drop_duplicate(self.df)
        self.assertTrue(not df.duplicated().any())
   
    def test_convert_to_datetime(self):
        df = self.cleaner.convert_to_datetime(self.df)
        self.assertTrue(type(df['start'].dtype == ptypes.DatetimeTZDtype))
        self.assertTrue(type(df['end'].dtype == ptypes.DatetimeTZDtype))

    def test_drop_columns_with_null_values(self):
       threshold_in_percent = 30
       Helper = TelecomHelper()

       null_percent_df = pd.DataFrame(columns=['column', 'null_percent'])
       columns = self.df.columns.values.tolist()

       null_percent_df['column'] = columns
       null_percent_df['null_percent'] = null_percent_df['column'].map(
           lambda x: Helper.percent_missing_for_col(self.df, x))

       columns_to_be_dropped = null_percent_df[null_percent_df['null_percent']
                                               > threshold_in_percent]['column'].to_list()
       cleaned_df = self.cleaner.drop_columns_with_null_values(
           self.df, threshold_in_percent)
       for col in columns_to_be_dropped:
           self.assertTrue(not col in cleaned_df)
           self.assertTrue(True)

    def test_drop_columns_with_null_values(self):
       threshold_in_percent = 1
       Helper = TelecomHelper()

       null_percent_df = pd.DataFrame(columns=['column', 'null_percent'])
       columns = self.df.columns.values.tolist()

       null_percent_df['column'] = columns
       null_percent_df['null_percent'] = null_percent_df['column'].map(
           lambda x: Helper.percent_missing_for_col(self.df, x))

       columns_subset = null_percent_df[null_percent_df['null_percent']
                                               < threshold_in_percent]['column'].to_list()
       
       cleaned_df = self.cleaner.drop_rows_with_null_values(
           self.df, threshold_in_percent)
       for col in columns_subset:
           self.assertTrue((cleaned_df[col].isna().sum() == 0))
    
    def test_handle_missing_qantitative_data_with_mean(self):
        numeric_data = ['int16', 'int32', 'int64',
                        'float16', 'float32', 'float64']

        all_cols = self.df.columns.to_list()
        num_cols = [c for c in all_cols if self.df[c].dtypes in numeric_data]

        cleaned_df = self.cleaner.handle_missing_qantitative_data_with_mean(self.df)

        
        for col in num_cols:
            self.assertTrue((cleaned_df[col].isna().sum() == 0))


if __name__ == '__main__':
    unittest.main()
