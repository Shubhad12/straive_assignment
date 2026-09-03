import pandas as pd
import numpy as np

# Input and output file paths
input_csv = 'payment_transaction.csv'
output_csv = 'cleaned_payment_transaction.csv'
chunk_size = 10000

# Control metrics
source_row_count = 0
clean_row_count = 0
duplicate_ids_removed = 0
invalid_amounts_removed = 0

seen_transaction_ids = set()
cleaned_chunks = []

# Step 1 & 2: Process file in chunks
for chunk in pd.read_csv(input_csv, chunksize=chunk_size):
    source_row_count += len(chunk)

    # Step 3: Remove duplicate transaction_ids
    chunk_no_dups = chunk.drop_duplicates(subset=['transaction_id'])
    duplicate_ids_removed += len(chunk) - len(chunk_no_dups)

    # Filter globally unique IDs across chunks
    chunk_unique = chunk_no_dups[~chunk_no_dups['transaction_id'].isin(seen_transaction_ids)].copy()
    seen_transaction_ids.update(chunk_unique['transaction_id'])

    # Step 4: Handle invalid amounts (must be > 0 and not null)
    valid_amount_mask = chunk_unique['amount'].notna() & (chunk_unique['amount'] > 0)
    invalid_amounts_removed += (~valid_amount_mask).sum()
    chunk_clean = chunk_unique[valid_amount_mask].copy()

    # Step 5: Convert date fields to standard datetime
    chunk_clean['transaction_date'] = pd.to_datetime(chunk_clean['transaction_date'], errors='coerce')

    # Step 6: Standardize categorical values (uppercase & trimmed)
    categorical_cols = ['channel', 'payment_type', 'status']
    for col in categorical_cols:
        if col in chunk_clean.columns:
            chunk_clean[col] = chunk_clean[col].astype(str).str.strip().str.upper()

    cleaned_chunks.append(chunk_clean)

# Combine all cleaned chunks
df_cleaned = pd.concat(cleaned_chunks, ignore_index=True)
clean_row_count = len(df_cleaned)

# Save cleaned output
df_cleaned.to_csv(output_csv, index=False)

# Step 7: Calculate customer-level aggregates
customer_aggregates = df_cleaned.groupby('account_id').agg(
    total_transactions=('transaction_id', 'count'),
    total_spend=('amount', 'sum'),
    avg_transaction_value=('amount', 'mean'),
    successful_transactions=('status', lambda x: (x == 'SUCCESS').sum())
).reset_index()

# Step 8: Reconciliation & Control Report
print("--- RECONCILIATION CONTROL REPORT ---")
print(f"Source Row Count:              {source_row_count}")
print(f"Clean Row Count:               {clean_row_count}")
print(f"Duplicate IDs Removed:         {duplicate_ids_removed}")
print(f"Invalid Amounts Removed:       {invalid_amounts_removed}")
print(f"Total Customer Accounts:       {len(customer_aggregates)}")
print(f"Total Reconciled Amount:       {df_cleaned['amount'].sum():.2f}")