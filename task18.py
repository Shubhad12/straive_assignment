import statsmodels.api as sm
from statsmodels.stats.proportion import proportion_effectsize

# Given parameters
p1 = 0.10  # Baseline conversion rate (10%)
p2 = 0.12  # Target conversion rate (12%)
alpha = 0.05
power = 0.80

# Calculate Cohen's h effect size
effect_size = proportion_effectsize(p1, p2)

# Calculate required sample size per group (two-sided test)
power_analysis = sm.stats.NormalIndPower()
n_required = power_analysis.solve_power(
    effect_size=effect_size,
    alpha=alpha,
    power=power,
    ratio=1.0,
    alternative='two-sided'
)

print("--- POWER & SAMPLE SIZE ANALYSIS ---")
print(f"Baseline Conversion (p1):       {p1*100:.1f}%")
print(f"Target Conversion (p2):         {p2*100:.1f}%")
print(f"Effect Size (Cohen's h):        {effect_size:.4f}")
print(f"Required Sample Size per Group:  {int(round(n_required)):,}")
print(f"Total Required Sample Size:     {int(round(n_required * 2)):,}")