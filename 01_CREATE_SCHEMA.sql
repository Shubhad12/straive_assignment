-- Create these tables in the learner's Oracle schema.
CREATE TABLE branch (
 branch_id VARCHAR2(10) PRIMARY KEY, branch_name VARCHAR2(100) NOT NULL,
 city VARCHAR2(50) NOT NULL, state VARCHAR2(50) NOT NULL, region VARCHAR2(30) NOT NULL);

CREATE TABLE customer (
 customer_id NUMBER PRIMARY KEY, customer_name VARCHAR2(100) NOT NULL,
 customer_segment VARCHAR2(30) NOT NULL, city VARCHAR2(50), state VARCHAR2(50),
 date_of_birth DATE, onboarding_date DATE, customer_status VARCHAR2(20));

CREATE TABLE customer_kyc (
 customer_id NUMBER PRIMARY KEY, kyc_status VARCHAR2(20), kyc_risk_rating VARCHAR2(20),
 annual_income NUMBER(15,2), occupation VARCHAR2(100), pep_flag CHAR(1), last_kyc_date DATE,
 CONSTRAINT fk_kyc_customer FOREIGN KEY(customer_id) REFERENCES customer(customer_id));

CREATE TABLE account (
 account_id NUMBER PRIMARY KEY, customer_id NUMBER NOT NULL, branch_id VARCHAR2(10) NOT NULL,
 account_type VARCHAR2(30), account_status VARCHAR2(20), opened_date DATE,
 current_balance NUMBER(15,2),
 CONSTRAINT fk_account_customer FOREIGN KEY(customer_id) REFERENCES customer(customer_id),
 CONSTRAINT fk_account_branch FOREIGN KEY(branch_id) REFERENCES branch(branch_id));

CREATE TABLE merchant (
 merchant_id VARCHAR2(20) PRIMARY KEY, merchant_name VARCHAR2(100),
 merchant_category VARCHAR2(50), merchant_city VARCHAR2(50), merchant_risk_rating VARCHAR2(20));

CREATE TABLE payment_transaction (
 transaction_id NUMBER PRIMARY KEY, account_id NUMBER NOT NULL, merchant_id VARCHAR2(20),
 branch_id VARCHAR2(10) NOT NULL, transaction_date TIMESTAMP NOT NULL,
 amount NUMBER(15,2), currency VARCHAR2(3), channel VARCHAR2(30), payment_type VARCHAR2(30),
 status VARCHAR2(20), failure_reason VARCHAR2(100), processing_time_sec NUMBER(10,2),
 device_id VARCHAR2(50), ip_risk_score NUMBER(5,2), transaction_risk_score NUMBER(5,2),
 feature_version VARCHAR2(10),
 CONSTRAINT fk_tx_account FOREIGN KEY(account_id) REFERENCES account(account_id),
 CONSTRAINT fk_tx_merchant FOREIGN KEY(merchant_id) REFERENCES merchant(merchant_id),
 CONSTRAINT fk_tx_branch FOREIGN KEY(branch_id) REFERENCES branch(branch_id));

CREATE TABLE payment_event (
 event_id NUMBER PRIMARY KEY, transaction_id NUMBER NOT NULL, event_type VARCHAR2(30) NOT NULL,
 event_timestamp TIMESTAMP NOT NULL, event_status VARCHAR2(20),
 CONSTRAINT fk_event_transaction FOREIGN KEY(transaction_id) REFERENCES payment_transaction(transaction_id));

CREATE TABLE fraud_alert (
 alert_id NUMBER PRIMARY KEY, transaction_id NUMBER NOT NULL, alert_timestamp TIMESTAMP,
 alert_type VARCHAR2(50), alert_score NUMBER(5,2), investigation_status VARCHAR2(30),
 confirmed_fraud_flag CHAR(1), investigator_id VARCHAR2(30),
 CONSTRAINT fk_alert_transaction FOREIGN KEY(transaction_id) REFERENCES payment_transaction(transaction_id));

CREATE TABLE experiment_assignment (
 experiment_id VARCHAR2(30), customer_id NUMBER, experiment_group VARCHAR2(20),
 assignment_date DATE, eligible_flag CHAR(1),
 PRIMARY KEY(experiment_id,customer_id),
 CONSTRAINT fk_exp_customer FOREIGN KEY(customer_id) REFERENCES customer(customer_id));

CREATE INDEX idx_tx_account ON payment_transaction(account_id);
CREATE INDEX idx_tx_date ON payment_transaction(transaction_date);
CREATE INDEX idx_tx_channel ON payment_transaction(channel);
CREATE INDEX idx_tx_status ON payment_transaction(status);
CREATE INDEX idx_event_transaction ON payment_event(transaction_id);
CREATE INDEX idx_alert_transaction ON fraud_alert(transaction_id);
