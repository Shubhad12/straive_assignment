import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load datasets
transactions = pd.read_csv('payment_transaction.csv')
accounts = pd.read_csv('ACCOUNT.csv')
kyc = pd.read_csv('CUSTOMER_KYC.csv')

# Merge to get all numerical features
merged_df = transactions.merge(accounts, on='account_id') \
                        .merge(kyc, on='customer_id')

# Select numerical columns for correlation analysis
corr_cols = [
    'amount', 
    'processing_time_sec', 
    'transaction_risk_score', 
    'ip_risk_score', 
    'annual_income'
]

# Calculate Pearson correlation matrix
corr_matrix = merged_df[corr_cols].corr()

print("--- Correlation Matrix ---")
print(corr_matrix.round(4))