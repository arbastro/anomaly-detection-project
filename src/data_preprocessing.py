import pandas as pd
from sklearn.preprocessing import StandardScaler

def load_data(file_path):
    """loads data from CSV"""
    return pd.read_csv(file_path)

def preprocess_data(df):
    """preprocesses the data by filling missing values and scaling features"""
    df.fillna(df.mean(), inplace=True)
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(df)
    return pd.DataFrame(scaled_data, columns=df.columns)

if __name__ == "__main__":
    df = load_data("../data/sample_data.csv")
    preprocessed_df = preprocess_data(df)
    print(preprocessed_df.head())
