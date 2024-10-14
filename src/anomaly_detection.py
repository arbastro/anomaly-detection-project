import numpy as np
from sklearn.ensemble import IsolationForest

def detect_anomalies(df):
    """detects anomalies using Isolation Forest"""
    model = IsolationForest(contamination=0.05)
    df['anomaly'] = model.fit_predict(df)
    anomalies = df[df['anomaly'] == -1]
    return anomalies

if __name__ == "__main__":
    from data_preprocessing import preprocess_data, load_data
    df = load_data("../data/sample_data.csv")
    preprocessed_df = preprocess_data(df)
    anomalies = detect_anomalies(preprocessed_df)
    print("anomalies detected:")
    print(anomalies)
