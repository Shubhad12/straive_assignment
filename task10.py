import pandas as pd
import numpy as np

# Load transaction dataset
df = pd.read_csv('payment_transaction.csv')

# Calculate descriptive statistics for transaction amount
amount = df['amount']

stats_data = {
    'Metric': [
        'Mean', 'Median', 'Mode', 'Variance', 'Standard Deviation',
        'Q1 (25th Percentile)', 'Q3 (75th Percentile)', 'IQR (Interquartile Range)',
        'P90 (90th Percentile)', 'P95 (95th Percentile)', 'P99 (99th Percentile)', 'Skewness'
    ],
    'Value': [
        amount.mean(),
        amount.median(),
        amount.mode()[0],
        amount.var(),
        amount.std(),
        amount.quantile(0.25),
        amount.quantile(0.75),
        amount.quantile(0.75) - amount.quantile(0.25),
        amount.quantile(0.90),
        amount.quantile(0.95),
        amount.quantile(0.99),
        amount.skew()
    ]
}

stats_df = pd.DataFrame(stats_data)
stats_df['Value'] = stats_df['Value'].round(2)
print(stats_df.to_string(index=False))