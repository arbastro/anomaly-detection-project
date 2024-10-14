# anomaly-detection-project
this is just for testing thingy
anyways proper readme:
# Anomaly Detection Project

## Overview
># ⚠️ | THIS IS A WORK-IN-PROGRESS AND ISN'T MEANT TO BE RELEASED TO PUBLIC YET
Performs anomaly detection on a sample dataset using Isolation Forest - data is processed, anomalies are detected, and results are saved to a SQLite database.

---
## Setup Instructions

1. Clone this repository:
```bash
git clone https://github.com/arbastro/anomaly-detection-project.git
```

2. Navigate to the project directory:
```bash
cd anomaly-detection-project
```

3. Install the required dependencies:
```bash
pip install -r requirements.txt
```

4. Run the preprocessing and anomaly detection:
```bash
python src/anomaly_detection.py
```

5. Open the notebook for interactive analysis:
```bash
jupyter notebook notebooks/anomaly_detection_analysis.ipynb
```
----
## Data
- The `sample_data.csv` file contains a synthetic dataseta
- The `database.sqlite` stores anomalies detected from the data

## Features
- Isolation Forest-based anomaly detection
- SQLite database integration for storing and retrieving results
---

# stuff for myself
i. because the `anomaly_detection_analysis.ipynb` file in the `notebooks` folder is giving me an Invalid Notebook error, all i have backed up is an older version which i will save here:

```ipynb
# anomaly detection analysis - jupyter notebook
#interactive analysis of anomalies detected using the Isolation Forest algorithm

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler

#'../data/sample_data.csv'
df = pd.read_csv('../data/sample_data.csv')
print("data preview:")
df.head()

#data preprocessing
#fills missing values and scales data
print("preprocessing data...")
df.fillna(df.mean(), inplace=True)
scaler = StandardScaler()
scaled_data = scaler.fit_transform(df)
df_scaled = pd.DataFrame(scaled_data, columns=df.columns)
print("preprocessed data:")
df_scaled.head()

#isolation forest for anomaly detection
# tnitialize, train Isolation Forest model with contamination factor of 0.05.
print("detecting anomalies...")
model = IsolationForest(contamination=0.05)
df_scaled['anomaly'] = model.fit_predict(df_scaled)
anomalies = df_scaled[df_scaled['anomaly'] == -1]
print(f"anomalies detected: {len(anomalies)}")

#save anomalies to SQLite database
import sqlite3

def save_to_database(df, db_file):
    """save detected anomalies to SQLite database"""
    conn = sqlite3.connect(db_file)
    df.to_sql('anomalies', conn, if_exists='replace', index=False)
    conn.close()

db_file = "../data/database.sqlite"
print(f"saving anomalies to {db_file}...")
save_to_database(anomalies, db_file)

#simple visualization of anomalies in the dataset.
print("visualizing anomalies...")
plt.scatter(df_scaled.index, df_scaled['anomaly'], c=df_scaled['anomaly'], cmap='coolwarm', edgecolors='k')
plt.title('Anomaly Detection Visualization')
plt.xlabel('Index')
plt.ylabel('Anomaly (-1 = Anomalous, 1 = Normal)')
plt.show()

#fetch anomalies from database (this is really optional)
def fetch_from_database(db_file):
    """fetch data from SQLite database"""
    conn = sqlite3.connect(db_file)
    query = "SELECT * FROM anomalies"
    df = pd.read_sql(query, conn)
    conn.close()
    return df

print("fetching anomalies from database for verification...")
fetched_anomalies = fetch_from_database(db_file)
print(f"Fetched {len(fetched_anomalies)} anomalies from database.")
fetched_anomalies.head()

# this is end of analysis
# Hm. Serous. Ok. Pro OkUes?
```
