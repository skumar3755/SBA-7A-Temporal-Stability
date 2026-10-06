# Temporal Stability of Credit-Risk Factors in SBA 7(a) Lending

## Data Analytics Capstone

### Research Topic

**Temporal Stability of Credit-Risk Factors in SBA 7(a) Lending**

---

## 1. Project Overview

This project examines whether approval-time credit-risk factors associated with subsequent SBA 7(a) loan charge-off remain stable across lending cohorts and whether changes in these relationships affect predictive reliability and risk classification.

The study uses publicly available U.S. Small Business Administration (SBA) 7(a) loan-level data and focuses on information available at or around the time of loan approval.

The central analytical problem is temporal stability: a credit-risk relationship identified from historical lending data may change as borrower characteristics, lending practices, economic conditions, and portfolio composition evolve.

The study therefore progresses from identifying approval-time risk factors to examining their temporal stability, testing out-of-time predictive performance, and evaluating the implications for risk classification.

---

## 2. Business Problem

Small-business lenders use borrower, business, loan, lender, industry, and geographic characteristics available at or around loan approval to assess credit risk.

However, relationships between these approval-time characteristics and subsequent loan charge-off may change across lending cohorts. If these relationships change, a model developed using historical data may become less reliable when applied to subsequent borrowers.

This study investigates whether approval-time credit-risk relationships remain stable over time and whether changes in those relationships affect predictive performance and charge-off classification.

---

## 3. Purpose of the Study

The purpose of this quantitative study is to examine the temporal stability of approval-time characteristics associated with 36-month charge-off risk in SBA 7(a) lending and to evaluate whether changes in these relationships affect predictive reliability and risk classification performance across sufficiently mature lending cohorts.

The study will:

1. Identify approval-time characteristics associated with 36-month charge-off risk.
2. Examine whether relationships between important risk characteristics and charge-off risk differ across lending cohorts.
3. Evaluate whether a credit-risk model developed using an earlier cohort maintains predictive performance when applied to a subsequent out-of-time cohort.
4. Examine whether changes in predictive performance affect charge-off classification across prespecified risk-classification thresholds.

---

## 4. Research Questions and Hypotheses

### RQ1

**Which approval-time characteristics are significantly associated with 36-month SBA 7(a) loan charge-off risk?**

**H01:** Approval-time characteristics are not significantly associated with 36-month SBA 7(a) loan charge-off risk.

**H11:** At least one approval-time characteristic is significantly associated with 36-month SBA 7(a) loan charge-off risk.

### RQ2

**To what extent do the associations between approval-time credit-risk characteristics and 36-month SBA 7(a) loan charge-off risk differ across sufficiently mature lending cohorts?**

**H02:** Associations between approval-time credit-risk characteristics and 36-month SBA 7(a) loan charge-off risk do not significantly differ across sufficiently mature lending cohorts.

**H12:** At least one association between an approval-time credit-risk characteristic and 36-month SBA 7(a) loan charge-off risk significantly differs across sufficiently mature lending cohorts.

### RQ3

**Does a credit-risk model developed using an earlier sufficiently mature SBA 7(a) lending cohort maintain its predictive performance when applied to a subsequent sufficiently mature lending cohort?**

**H03:** The credit-risk model does not show a statistically significant difference in predictive performance between the earlier validation cohort and the subsequent out-of-time cohort.

**H13:** The credit-risk model shows a statistically significant difference in predictive performance between the earlier validation cohort and the subsequent out-of-time cohort.

### RQ4

**To what extent do differences in predictive performance between sufficiently mature SBA 7(a) lending cohorts alter charge-off classification performance across prespecified risk-classification thresholds?**

**H04:** Charge-off classification performance does not significantly differ between the validation and subsequent out-of-time cohorts across the prespecified classification thresholds.

**H14:** Charge-off classification performance significantly differs between the validation and subsequent out-of-time cohorts across at least one prespecified classification threshold.

---

## 5. Data Source

The primary data source is the U.S. Small Business Administration (SBA) **7(a) & 504 FOIA** open-data portal.

Official source:

https://data.sba.gov/dataset/7a-504-foia

The SBA provides separate 7(a) files by fiscal-year period and a supporting data dictionary. The dataset is updated quarterly.

This study uses the **7(a) FY2020-Present** loan-level data.

The source dataset used for the current study contains:

- 388,338 observations
- 42 variables
- Approval dates from October 1, 2019 through June 30, 2026

The unit of analysis is the individual SBA 7(a) loan record.

---

## 6. Analytical Outcome

The primary outcome is a binary indicator of whether a loan is charged off within 36 months of its approval date.

### Outcome definition

```text
Y = 1 if CHGOFF occurs within 36 months of approval
Y = 0 if CHGOFF does not occur within the 36-month analytical horizon
