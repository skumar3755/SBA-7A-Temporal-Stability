# Data

This directory contains the datasets and data documentation used in the  Data Analytics Capstone.

The study uses publicly available U.S. Small Business Administration (SBA) 7(a) loan-level data.

## Data structure

- `raw/` — original source data, subject to applicable SBA data-use and redistribution requirements.
- `processed/` — analytical datasets generated through the documented data-processing workflow.
- `data_dictionary.csv` — analytical data dictionary describing variables used in the study.

The analytical dataset is constructed using approval-time information and a 36-month charge-off outcome while excluding variables that create outcome leakage.
