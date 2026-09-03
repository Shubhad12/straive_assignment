import pandas as pd
from scipy import stats

# Load payment transaction data
df = pd.read_csv('payment_transaction.csv')

# Create Contingency Table: Channel vs Status
contingency_table = pd.crosstab(df['channel'], df['status'])

# Run Chi-Square Test
chi2_stat, p_val, dof, expected = stats.chi2_contingency(contingency_table)

alpha = 0.05
decision = "Reject H0 (Statistically Associated)" if p_val < alpha else "Fail to Reject H0 (No Association)"

print("--- Contingency Table ---")
print(contingency_table)
print("\n--- Chi-Square Test Results ---")
print(f"Chi-Square Statistic: {chi2_stat:.4f}")
print(f"Degrees of Freedom: {dof}")
print(f"p-value: {p_val:.4e}")
print(f"Decision (alpha=0.05): {decision}")