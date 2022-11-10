import numpy as np
import pandas as pd
from sklearn.preprocessing import Normalizer, MinMaxScaler


class TelecomHelper:
  
  def __init__(self):
    pass
  
  def read_csv(self, csv_path, missing_values=[]):
    try:
        df = pd.read_csv(csv_path, na_values=missing_values)
        print("file read as csv")
        return df
    except FileNotFoundError:
        print("file not found")
  
  def save_csv(self, df, csv_path):
    try:
        df.to_csv(csv_path, index=False)
        print('File Successfully Saved.!!!')

    except Exception:
        print("Save failed...")

    return df
    
  def percent_missing(self, df: pd.DataFrame) -> float:

    totalCells = np.product(df.shape)
    missingCount = df.isnull().sum()
    totalMissing = missingCount.sum()
    return round((totalMissing / totalCells) * 100, 2)
  
  def percent_missing_for_col(self, df: pd.DataFrame, col_name: str) -> float:
    total_count = len(df[col_name])
    if total_count <= 0:
        return 0.0
    missing_count = df[col_name].isnull().sum()

    return round((missing_count / total_count) * 100, 2)
  
  def convert_bytes_to_megabytes(self, df: pd.DataFrame, bytes_data):

    megabyte = 1*10e+5
    megabyte_col = df[bytes_data] / megabyte

    return megabyte_col
  
  def normalizer(self, df, columns):
    norm = Normalizer()
    return pd.DataFrame(norm.fit_transform(df), columns=columns)


  def scaler(self, df, columns):
    minmax_scaler = MinMaxScaler()
    return pd.DataFrame(minmax_scaler.fit_transform(df), columns=columns)


  def scale_and_normalize(self, df, columns):
    return self.normalizer(self.scaler(df, columns), columns)
  
  

  
  
