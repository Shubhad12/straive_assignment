BANKING & PAYMENTS 4-HOUR CASE STUDY DATASET

Static dataset: learners do NOT need Python to generate data.

Volumes:
CUSTOMER: 10,000
CUSTOMER_KYC: 10,000
ACCOUNT: 15,000
BRANCH: 20
MERCHANT: 500
PAYMENT_TRANSACTION: 50,000
PAYMENT_EVENT: 150,000
FRAUD_ALERT: 3,174
EXPERIMENT_ASSIGNMENT: 8,000

Intentional issues planted for investigation:
- 100 null merchant IDs
- 60 zero/negative transaction amounts
- 50 out-of-range risk scores
- 250 processing-time anomalies
- 120 late-arriving payment events

Files:
01_CREATE_SCHEMA.sql
DATA_DICTIONARY.csv
BRANCH.csv
CUSTOMER.csv
CUSTOMER_KYC.csv
ACCOUNT.csv
MERCHANT.csv
PAYMENT_TRANSACTION.csv
PAYMENT_EVENT.csv
FRAUD_ALERT.csv
EXPERIMENT_ASSIGNMENT.csv

Oracle load order:
BRANCH -> CUSTOMER -> CUSTOMER_KYC -> ACCOUNT -> MERCHANT ->
PAYMENT_TRANSACTION -> PAYMENT_EVENT -> FRAUD_ALERT -> EXPERIMENT_ASSIGNMENT

Use Oracle SQL Developer Import Data or SQL*Loader.
Do not clean or modify the CSVs before performing the data-quality tasks.

SQL INSERT LOAD
===============
A complete Oracle INSERT ALL implementation is provided in sql_insert_scripts/.

1. Run 01_CREATE_SCHEMA.sql.
2. Open sql_insert_scripts/00_LOAD_ALL_DATA.sql in Oracle SQL Developer.
3. Run with F5 / Run Script.
4. Run sql_insert_scripts/03_VALIDATE_LOAD.sql.

The INSERT scripts use batches of 500 rows and periodic COMMITs.
Do not run the load twice unless the target tables are cleared first.
