# Code

This directory contains the reproducible analysis scripts for the QM 640 Data Analytics Capstone.

The analysis is organized sequentially according to the study methodology:

1. `01_data_import.py` — Import and inspect the source data.
2. `02_data_quality.py` — Assess data quality, missingness, duplicates, and date consistency.
3. `03_cohort_construction.py` — Construct the 36-month analytical population and lending cohorts.
4. `04_feature_engineering.py` — Create approval-time analytical variables and exclude information leakage.
5. `05_sample_size.py` — Document the sample-size calculations.
6. `06_rq1_logistic.py` — Analyze approval-time characteristics associated with 36-month charge-off risk.
7. `07_rq2_temporal_stability.py` — Analyze cohort-by-risk-factor interactions and temporal stability.
8. `08_rq3_oot_validation.py` — Conduct chronological out-of-time predictive validation.
9. `09_rq4_threshold_analysis.py` — Evaluate classification performance across prespecified risk thresholds.

All scripts will be documented so that the analytical workflow can be reproduced from the available source data and documented processing steps.
