from pathlib import Path

import pandas as pd


# Project paths
PROJECT_ROOT = Path(__file__).resolve().parents[1]

DATA_FILE = (
    PROJECT_ROOT
    / "data"
    / "raw"
    / "FOIA_7a_FY2020_Present_asof_260930.csv"
)

OUTPUT_DIR = PROJECT_ROOT / "outputs" / "tables"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def main():
    print("Loading SBA 7(a) source data...")
    print(f"Source file: {DATA_FILE}")

    if not DATA_FILE.exists():
        raise FileNotFoundError(
            f"Source file not found: {DATA_FILE}"
        )

    # Import the complete source file.
    # low_memory=False provides consistent type inference across columns.
    data = pd.read_csv(DATA_FILE, low_memory=False)

    print("Source data loaded successfully.")

    # Basic source-file verification
    row_count, column_count = data.shape

    print(f"Rows: {row_count:,}")
    print(f"Columns: {column_count:,}")

    # Convert analytical date fields for verification.
    date_columns = [
        "AsOfDate",
        "ApprovalDate",
        "FirstDisbursementDate",
        "PaidInFullDate",
        "ChargeOffDate",
    ]

    for column in date_columns:
        if column in data.columns:
            data[column] = pd.to_datetime(
                data[column],
                errors="coerce",
            )

    # Source-file profile
    approval_min = data["ApprovalDate"].min()
    approval_max = data["ApprovalDate"].max()
    snapshot_dates = data["AsOfDate"].dropna().unique()

    profile = pd.DataFrame(
        {
            "Measure": [
                "Source filename",
                "Number of records",
                "Number of variables",
                "Earliest approval date",
                "Latest approval date",
                "Number of snapshot dates",
            ],
            "Value": [
                DATA_FILE.name,
                f"{row_count}",
                f"{column_count}",
                str(approval_min.date()) if pd.notna(approval_min) else "",
                str(approval_max.date()) if pd.notna(approval_max) else "",
                f"{len(snapshot_dates)}",
            ],
        }
    )

    # Column and inferred data-type summary
    column_summary = pd.DataFrame(
        {
            "Variable": data.columns,
            "ImportedDataType": [
                str(data[column].dtype) for column in data.columns
            ],
            "NonMissingCount": [
                int(data[column].notna().sum())
                for column in data.columns
            ],
            "MissingCount": [
                int(data[column].isna().sum())
                for column in data.columns
            ],
            "UniqueValues": [
                int(data[column].nunique(dropna=True))
                for column in data.columns
            ],
        }
    )

    column_summary["MissingPercent"] = (
        column_summary["MissingCount"] / row_count * 100
    ).round(2)

    # Fiscal-year summary
    fiscal_year_summary = (
        data.groupby("ApprovalFY", dropna=False)
        .size()
        .reset_index(name="LoanCount")
        .sort_values("ApprovalFY")
    )

    fiscal_year_summary["PercentOfSource"] = (
        fiscal_year_summary["LoanCount"] / row_count * 100
    ).round(2)

    # Loan-status summary
    status_summary = (
        data.groupby("LoanStatus", dropna=False)
        .size()
        .reset_index(name="LoanCount")
        .sort_values("LoanCount", ascending=False)
    )

    status_summary["PercentOfSource"] = (
        status_summary["LoanCount"] / row_count * 100
    ).round(2)

    # Exact duplicate-row count
    exact_duplicates = int(data.duplicated().sum())

    duplicate_summary = pd.DataFrame(
        {
            "Measure": ["Exact duplicate rows"],
            "Value": [exact_duplicates],
        }
    )

    # Save outputs
    profile.to_csv(
        OUTPUT_DIR / "table_01_source_file_profile.csv",
        index=False,
    )

    column_summary.to_csv(
        OUTPUT_DIR / "table_02_variable_profile.csv",
        index=False,
    )

    fiscal_year_summary.to_csv(
        OUTPUT_DIR / "table_03_approval_fy_counts.csv",
        index=False,
    )

    status_summary.to_csv(
        OUTPUT_DIR / "table_04_loan_status_counts.csv",
        index=False,
    )

    duplicate_summary.to_csv(
        OUTPUT_DIR / "table_05_exact_duplicate_count.csv",
        index=False,
    )

    print("\nSource-file verification completed.")
    print(f"Approval-date range: {approval_min} to {approval_max}")
    print(f"Exact duplicate rows: {exact_duplicates:,}")
    print(f"Outputs saved to: {OUTPUT_DIR}")

    print("\nApproval fiscal-year counts:")
    print(fiscal_year_summary.to_string(index=False))

    print("\nLoan-status counts:")
    print(status_summary.to_string(index=False))


if __name__ == "__main__":
    main()
