import sqlite3
import pandas as pd

def create_connection(db_file):
    """create database connection"""
    conn = sqlite3.connect(db_file)
    return conn

def save_to_database(df, db_file):
    """saves the dataframe to  SQLite database"""
    conn = create_connection(db_file)
    df.to_sql('anomalies', conn, if_exists='replace', index=False)
    conn.close()

def fetch_from_database(db_file):
    """fetches data from  SQLite database"""
    conn = create_connection(db_file)
    query = "SELECT * FROM anomalies"
    df = pd.read_sql(query, conn)
    conn.close()
    return df

if __name__ == "__main__":
    from anomaly_detection import detect_anomalies
    from data_preprocessing import preprocess_data, load_data
    
    df = load_data("../data/sample_data.csv")
    preprocessed_df = preprocess_data(df)
    anomalies = detect_anomalies(preprocessed_df)
    
    db_file = "../data/database.sqlite"
    save_to_database(anomalies, db_file)
    
    print("data saved to database")
