import pandas as pd
import numpy as np

data = {
    "customer_id": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 101],
    "customer_name": [
        " Amit Sharma ",
        "PRIYA MEHTA",
        "Rahul Shah",
        None,
        "Neha Verma",
        "rohan patil",
        "Sneha Joshi",
        " Vikas Gupta",
        "Anjali Rao",
        "Karan Malhotra",
        "Amit Sharma",
    ],
    "email": [
        "amit@banku.com",
        "priya@banku.com",
        "rahul@banku.com",
        None,
        "neha@banku.com",
        "rohan@banku.com",
        "sneha@banku.com",
        "vikas@banku.com",
        "anjali@banku.com",
        "karan@banku.com",
        "amit@banku.com",
    ],
    "phone": [
        "+91-98765-43210",
        "9876543211",
        "98765 43212",
        None,
        "+91-9876543213",
        "98765-43214",
        "9876543215",
        "98765 43216",
        "+91 9876543217",
        "9876543217",
        "+91-98765-43210",
    ],
    "city": [
        "Pune",
        "Mumbai",
        "PUNE",
        "Gurugram",
        "Mumbai",
        None,
        "Delhi",
        "Bangalore",
        "Hyderabad",
        "Mumbai",
        "Pune",
    ],
    "customer_segment": [
        "Premium",
        "retail",
        "PREMIUM",
        "Retail",
        "Premium Customer",
        "RETAIL",
        "Premium",
        None,
        "Retail",
        "PREM",
        "Premium",
    ],
    "risk_score": [
        "25",
        "45",
        "70",
        "30",
        "85",
        "invalid",
        "40",
        None,
        "55",
        "120",
        "25",
    ],
    "balances": [
        "50000",
        "75000",
        "25000",
        "90000",
        "150000",
        "45000",
        "70000",
        "30000",
        "invalid",
        "110000",
        "50000",
    ],
    "created_date": [
        "2026-01-15",
        "15/01/2026",
        "2026-02-01",
        "2026-02-05",
        "05-02-2026",
        "2026-02-10",
        "2026/02/15",
        "1016-02-20",
        "2026-02-22",
        "2026-03-01",
        "2026-01-15",
    ],
    "updated_at": [
        "2026-08-20 10:00:00",
        "2026-08-20 11:00:00",
        "2026-08-20 12:00:00",
        "2026-08-20 13:00:00",
        "2026-08-20 14:00:00",
        "2026-08-20 15:00:00",
        "2026-08-20 16:00:00",
        "2026-08-20 17:00:00",
        "2026-08-20 18:00:00",
        "2026-08-20 19:00:00",
        "2026-08-21 10:00:00",
    ],
}

df = pd.DataFrame(data)

# print(df.shape)
# print(df.columns.tolist())
# print(df.dtypes)
# print(df.describe(include="all"))
# print(df.isnull().sum())
# missing_percentage = (df.isnull().sum() / len(df) * 100)
# print(missing_percentage)
# print(df[df["customer_name"].isnull()])
# df["customer_segment"] = df["customer_segment"].fillna("UNKNOWN")
# df["balances"] = df["balances"].fillna(0)

print(df["balances"].dtype)
df["balances"] = pd.to_numeric(df["balances"], errors="coerce")
print(df["balances"].dtype)



df["customer_name"]=(df["customer_name"].astype("string").str.strip().str.title())
df["email"]=(df["email"].astype("string").str.strip().str.lower())
df["city"]=(df["city"].astype("string").str.strip().str.title())
df["phone"]=(df["phone"].astype("string").str.replace(r"\D","", regex=True))
print(df.head(11))

invalid_risk = df[(df["risk_score"]<0) | (df["risk_score"]>100)]
print(invalid_risk)
invalid_balance = df[df["balances"]<0]
print(invalid_balance)

print(df.duplicated().sum())
print(df.duplicated(subset=["customer_id"]).sum())
print(df[df.duplicated(subset=["customer_id"],keep=False)])


df=df.sort_values("updated_at")
df=df.drop_duplicates(subset=["customer_id"], keep="last")
print(df["customer_id"].is_unique)
