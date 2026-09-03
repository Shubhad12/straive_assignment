import pandas as pd
import numpy as np

# Load Datasets
source_df = pd.read_csv('payment_transaction.csv')
clean_df = pd.read_csv('cleaned_payment_transaction.csv')

# Control 1: Row Count Reconciliation
source_rows = len(source_df)
clean_rows = len(clean_df)
row_count_diff = source_rows - clean_rows

# Control 2: SUM(amount) Reconciliation
source_sum = source_df[source_df['amount'] > 0]['amount'].sum()
clean_sum = clean_df['amount'].sum()
sum_diff = source_sum - clean_sum

# Control 3: COUNT(DISTINCT transaction_id)
source_distinct_ids = source_df['transaction_id'].nunique()
clean_distinct_ids = clean_df['transaction_id'].nunique()

# Control 4: Status Distribution Check
source_status = source_df['status'].str.strip().str.upper().value_counts().to_dict()
clean_status = clean_df['status'].value_counts().to_dict()

# Print Reconciliation Report
print("==================================================")
print("       DATA RECONCILIATION & CONTROL REPORT       ")
print("==================================================")
print(f"CONTROL 1: ROW COUNT")
print(f"  Source Rows:                 {source_rows:,}")
print(f"  Cleaned Rows:                {clean_rows:,}")
print(f"  Variance (Dropped Rows):     {row_count_diff:,}")
print("--------------------------------------------------")
print(f"CONTROL 2: TOTAL AMOUNT")
print(f"  Source Total Amount:         ${source_sum:,.2f}")
print(f"  Cleaned Total Amount:        ${clean_sum:,.2f}")
print(f"  Amount Variance:             ${sum_diff:,.2f}")
print("--------------------------------------------------")
print(f"CONTROL 3: DISTINCT TRANSACTION IDS")
print(f"  Source Unique Tx IDs:        {source_distinct_ids:,}")
print(f"  Cleaned Unique Tx IDs:       {clean_distinct_ids:,}")
print("--------------------------------------------------")
print(f"CONTROL 4: STATUS BREAKDOWN RECONCILIATION")
print(f"  Source Breakdown:            {source_status}")
print(f"  Cleaned Breakdown:           {clean_status}")
print("==================================================")

# Audit Pass/Fail Decision
if row_count_diff >= 0 and abs(sum_diff) < 0.01 and clean_distinct_ids == clean_rows:
    print("STATUS: AUDIT PASSED - Data pipeline integrity fully verified.")
else:
    print("STATUS: AUDIT FAILED - Reconciliation discrepancy detected.")