# Raw Data

This folder contains the original source data used in the project.

## Data Source

- **Publisher:** U.S. Small Business Administration
- **Dataset:** 7(a) and 504 Freedom of Information Act data
- **Selected file:** 7(a) FY2020–Present
- **Snapshot date:** 30 June 2026
- **Official source:** [SBA 7(a) and 504 FOIA Open Data](https://data.sba.gov/dataset/7a-504-foia)

## Source File

The source file contains SBA 7(a) loan-level records approved from
FY2020 onwards. The original file is retained without analytical
modification and is managed through Git Large File Storage because of
its size.

The source file will be used to generate the processed analytical data
through the documented scripts in the `code/` directory.

## Data-Handling Principles

- The raw source file will not be edited manually.
- All cleaning and transformations will be performed through
  reproducible Python scripts.
- Borrower names, street addresses, and other unnecessary identifiers
  will not be used as predictive features.
- Outcome-revealing variables will be used only for outcome construction
  and data-quality validation.
- The processed analytical dataset will be stored separately in
  `data/processed/`.

## Reproduction

To reproduce the analysis:

1. Retrieve the complete source file through Git Large File Storage or
   download it from the official SBA source.
2. Store the source file in this directory.
3. Run the scripts in the sequence documented in `code/README.md`.

The original source data remain subject to the definitions and
limitations described in the official SBA data dictionary.
