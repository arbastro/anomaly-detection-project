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
