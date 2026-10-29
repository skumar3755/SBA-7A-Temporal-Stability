# Temporal Stability of Credit-Risk Factors in SBA 7(a) Lending

## Data Analytics Capstone

**QM640: Data Analytics Capstone**

**T Suresh Kumar**

---

## Project Overview

This project examines whether approval-time credit-risk factors associated
with charge-off within 36 months of SBA 7(a) loan approval remain stable
across lending cohorts.

The study identifies relevant risk factors, tests whether their relationships
with charge-off change over time, evaluates out-of-time predictive
performance, and compares classification performance at prespecified
probability thresholds.

The findings are intended to support credit-risk monitoring, model
validation, recalibration, and risk-classification review. The study does
not make causal claims or propose operational loan-approval thresholds.

## Research Questions

## Final Research Questions and Hypotheses

### RQ1: Risk-Factor Identification

**Research question:** Which approval-time credit-risk factors are
independently associated with charge-off within 36 months of SBA 7(a)
loan approval?

**H0₁:** None of the selected factors is significantly associated with
36-month charge-off.

**H1₁:** At least one selected factor is significantly associated with
36-month charge-off.

**Method:** Multivariable logistic regression.

### RQ2: Temporal Stability

**Research question:** Do the relationships between selected
approval-time credit-risk factors and 36-month charge-off differ across
eligible lending cohorts?

**H0₂:** The selected risk-factor relationships do not differ across
eligible lending cohorts.

**H1₂:** At least one selected risk-factor relationship differs across
eligible lending cohorts.

**Method:** Logistic regression with cohort-by-predictor interaction
terms.

### RQ3: Out-of-Time Predictive Stability

**Research question:** Does ROC-AUC differ between the FY2021 validation
cohort and the FY2022–FY2023 out-of-time cohort?

**H0₃:** ROC-AUC does not differ between the two evaluation cohorts.

**H1₃:** ROC-AUC differs between the two evaluation cohorts.

**Method:** Independent-cohort comparison of ROC-AUC.

### RQ4: Classification Stability

**Research question:** Do classification-performance metrics differ
between the validation and out-of-time cohorts at predicted-probability
thresholds of 0.5%, 1%, 2%, 5%, and 10%?

**H0₄:** Classification performance does not differ between the two
evaluation cohorts at the prespecified thresholds.

**H1₄:** Classification performance differs between the two evaluation
cohorts at one or more prespecified thresholds.

**Method:** Comparison of sensitivity, specificity, positive predictive
value, false-positive rate, and false-negative rate.

## Data Source

The project uses the publicly available U.S. Small Business Administration
7(a) Freedom of Information Act loan-level dataset.

- **Resource:** 7(a) FY2020–Present
- **Snapshot date:** 30 June 2026
- **Unit of analysis:** Individual SBA 7(a) loan record
- **Official source:** [SBA 7(a) and 504 FOIA Open Data](https://data.sba.gov/dataset/7a-504-foia)

The locally stored source file contains 388,338 observations and 42
variables. 

## Analytical Outcome

The primary outcome indicates whether an eligible loan experienced a
qualifying charge-off within 36 months of approval.

- **Y = 1:** A qualifying charge-off occurred within 36 months.
- **Y = 0:** Sufficient follow-up confirms that no qualifying charge-off
  occurred within 36 months.

A missing `ChargeOffDate` alone is not treated as evidence of a non-event.

The outcome is constructed using `ApprovalDate`, `LoanStatus`,
`ChargeOffDate`, and other relevant outcome fields. These fields are not
used as model predictors.

Because the source snapshot is dated 30 June 2026, the primary analysis
requires approval on or before 30 June 2023 to provide a complete 36-month
observation period.

## Analytical Cohorts

The chronological design uses:

- **FY2020:** Model development
- **FY2021:** Model validation and selection
- **Mature FY2022–FY2023 observations:** Out-of-time evaluation

Cancelled loans, committed-but-undisbursed loans, immature observations,
and records with unresolved status-date inconsistencies will be excluded.

## Initial Predictor Set

| Predictor | Coding | Parameters |
|---|---|---:|
| `GrossApproval` | Continuous, initially linear | 1 |
| `InitialInterestRate` | Continuous, initially linear | 1 |
| `TermInMonths` | Continuous, initially linear | 1 |
| `RevolverStatus` | Binary | 1 |
| `CollateralInd` | Binary | 1 |
| `BusinessType` | Three categories | 2 |
| `BusinessAge` | Five categories, including Unknown/Missing | 4 |
| **Total** |  | **11** |


## Modelling and Validation

Logistic regression will be used for risk-factor identification,
interaction analysis, and as an interpretable predictive benchmark.

XGBoost will be considered for predictive modelling. Preprocessing and
model settings will be developed using FY2020, selected using FY2021, and
locked before evaluation on the out-of-time cohort.

Outcome-revealing fields and unnecessary borrower identifiers will be
excluded from the predictive feature set.

## Repository Structure

```text
SBA-7A-Temporal-Stability/
├── README.md
├── requirements.txt
├── code/
├── data/
│   ├── raw/
│   └── processed/
├── docs/
└── outputs/
    ├── figures/
    └── tables/
