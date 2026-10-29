# Data

This directory contains the datasets and data documentation used in this Data Analytics Capstone.

The study uses publicly available U.S. Small Business Administration
(SBA) 7(a) loan-level data.

## Directory Structure

- `raw/` contains the original SBA source data.
- `processed/` will contain analysis-ready datasets generated through
  the documented data-processing workflow.
- `7a_504_foia_data_dictionary.xlsx` contains the official SBA data
  dictionary.

## Analytical Data

The analytical dataset will be constructed using approval-time
information and a derived 36-month charge-off outcome.

Outcome-revealing variables and unnecessary borrower identifiers will
be excluded from the predictive feature set to prevent information
leakage and protect privacy.

Final processed datasets will document:

- Eligibility and exclusion rules
- Outcome construction
- Chronological cohort assignment
- Selected predictors and coding
- Missing-value treatment
- Data-quality decisions

The scripts used to create the processed data will be maintained in the
`code/` directory.
