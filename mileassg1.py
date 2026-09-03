import pandas as pd


def process_merchant_payments(merchant_file: str, payment_file: str):
    """Loads merchant and payment CSV files, cleans column headers,

    merges the data on 'merchant_id', and returns the merged DataFrame.
    """
    # 1. Load the CSV files
    df_merchants = pd.read_csv(merchant_file)
    df_payments = pd.read_csv(payment_file)

    # 2. Clean column headers by stripping leading/trailing whitespace
    df_merchants.columns = df_merchants.columns.str.strip()
    df_payments.columns = df_payments.columns.str.strip()

    # 3. Create lowercased header mappings to safely find 'merchant_id' regardless of case
    merchant_cols = {col.lower(): col for col in df_merchants.columns}
    payment_cols = {col.lower(): col for col in df_payments.columns}

    # 4. Verify that 'merchant_id' exists in both datasets
    if "merchant_id" not in merchant_cols:
        raise KeyError(
            f"'merchant_id' not found in {merchant_file}. Available columns: {list(df_merchants.columns)}"
        )
    if "merchant_id" not in payment_cols:
        raise KeyError(
            f"'merchant_id' not found in {payment_file}. Available columns: {list(df_payments.columns)}"
        )

    # 5. Extract actual column names (e.g., handles 'Merchant_ID', 'MERCHANT_ID', etc.)
    left_key = payment_cols["merchant_id"]
    right_key = merchant_cols["merchant_id"]

    # 6. Merge the DataFrames
    merged_df = pd.merge(
        df_payments,
        df_merchants,
        left_on=left_key,
        right_on=right_key,
        how="left",
    )

    return merged_df


# Example usage
if __name__ == "__main__":
    MERCHANT_FILE = "MERCHANT.csv"
    PAYMENT_FILE = "PAYMENT_EVENT.csv"

    try:
        df_result = process_merchant_payments(MERCHANT_FILE, PAYMENT_FILE)
        print("Data successfully merged! First 5 rows:")
        print(df_result.head())
    except Exception as e:
        print(f"Error during processing: {e}")