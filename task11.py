import pandas as pd
from scipy import stats

# Load payment transaction data
df = pd.read_csv('payment_transaction.csv')

# Filter for two payment channels/gateways to compare (e.g., MOBILE_APP vs WEB)
group1_data = df[df['channel'] == 'MOBILE_APP']['processing_time_sec'].dropna()
group2_data = df[df['channel'] == 'WEB']['processing_time_sec'].dropna()

# Calculate means
mean1 = group1_data.mean()
mean2 = group2_data.mean()
diff = mean1 - mean2

# Perform Welch's t-test (equal_var=False)
t_stat, p_value = stats.ttest_ind(group1_data, group2_data, equal_var=False)

# Decision based on alpha = 0.05
alpha = 0.05
decision = "Reject H0 (Statistically Significant Difference)" if p_value < alpha else "Fail to Reject H0 (No Significant Difference)"

# Output Results
print(f"Group 1 (MOBILE_APP) Mean: {mean1:.4f} sec")
print(f"Group 2 (WEB) Mean: {mean2:.4f} sec")
print(f"Mean Difference (Group 1 - Group 2): {diff:.4f} sec")
print(f"t-statistic: {t_stat:.4f}")
print(f"p-value: {p_value:.4e}")
print(f"Decision (alpha=0.05): {decision}")