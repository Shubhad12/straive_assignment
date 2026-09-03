import pandas as pd
from scipy import stats
from statsmodels.stats.multicomp import pairwise_tukeyhsd

# Load data
df = pd.read_csv('payment_transaction.csv')

# Group processing time by branch_id
branch_groups = [group['processing_time_sec'].dropna() for _, group in df.groupby('branch_id')]

# Run One-Way ANOVA
f_stat, p_val = stats.f_oneway(*branch_groups)

print("--- One-Way ANOVA Results ---")
print(f"F-Statistic: {f_stat:.4f}")
print(f"p-value: {p_val:.4e}")

# Post-Hoc Test (Tukey's HSD) if ANOVA is significant
if p_val < 0.05:
    clean_df = df.dropna(subset=['processing_time_sec', 'branch_id'])
    tukey = pairwise_tukeyhsd(endog=clean_df['processing_time_sec'], groups=clean_df['branch_id'], alpha=0.05)
    print("\n--- Tukey HSD Post-Hoc Test ---")
    print(tukey.summary())
    
    # Identify Best (Lowest processing time) & Worst (Highest processing time)
    branch_means = clean_df.groupby('branch_id')['processing_time_sec'].mean().sort_values()
    print(f"\nBest Performing Branch (Fastest): {branch_means.index[0]} ({branch_means.iloc[0]:.2f}s)")
    print(f"Worst Performing Branch (Slowest): {branch_means.index[-1]} ({branch_means.iloc[-1]:.2f}s)")