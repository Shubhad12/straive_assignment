import pandas as pd
import numpy as np
from statsmodels.stats.proportion import proportions_ztest

# Load data
df_exp = pd.read_csv('EXPERIMENT_ASSIGNMENT.csv')
df_tx = pd.read_csv('payment_transaction.csv')
df_acc = pd.read_csv('ACCOUNT.csv')

# Merge to get experiment performance for eligible customers
df_merged = df_exp[df_exp['eligible_flag'] == 'Y'].merge(df_acc, on='customer_id') \
                                                  .merge(df_tx, on='account_id')

# Aggregations per group
summary = df_merged.groupby('experiment_group').agg(
    total_users=('customer_id', 'nunique'),
    total_tx=('transaction_id', 'count'),
    successful_tx=('status', lambda x: (x == 'SUCCESS').sum())
).reset_index()

# Extract values
control_users = summary.loc[summary['experiment_group'] == 'CONTROL', 'total_users'].values[0]
treatment_users = summary.loc[summary['experiment_group'] == 'TREATMENT', 'total_users'].values[0]

control_succ = summary.loc[summary['experiment_group'] == 'CONTROL', 'successful_tx'].values[0]
control_total = summary.loc[summary['experiment_group'] == 'CONTROL', 'total_tx'].values[0]

treat_succ = summary.loc[summary['experiment_group'] == 'TREATMENT', 'successful_tx'].values[0]
treat_total = summary.loc[summary['experiment_group'] == 'TREATMENT', 'total_tx'].values[0]

# Calculate conversion (completion) rates
control_conv = control_succ / control_total
treat_conv = treat_succ / treat_total

# Metrics
abs_uplift = treat_conv - control_conv
rel_uplift = (abs_uplift / control_conv) * 100

# Two-proportion z-test
count = np.array([treat_succ, control_succ])
nobs = np.array([treat_total, control_total])
z_stat, p_value = proportions_ztest(count, nobs)

print(f"Control Users:           {control_users:,}")
print(f"Treatment Users:         {treatment_users:,}")
print(f"Control Conversion:      {control_conv * 100:.2f}%")
print(f"Treatment Conversion:    {treat_conv * 100:.2f}%")
print(f"Absolute Uplift:         {abs_uplift * 100:.2f}% points")
print(f"Relative Uplift:         {rel_uplift:.2f}%")
print(f"Z-statistic:             {z_stat:.4f}")
print(f"p-value:                 {p_value:.4e}")
print(f"Significant (alpha=0.05): {'YES' if p_value < 0.05 else 'NO'}")