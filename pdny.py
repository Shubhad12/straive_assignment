import pandas as pd
import numpy as ny

#print(pd.__version__)
#print(ny.__version__)

customer = {
    "customer_id" : [101,102,103,104],
    "customer_name" : ["Amit Sharma","Priya Gupta", "Rahul Shah", "Neha"],
    "City" : ["mumbai","gurgram","pune","bangalore"],
    "balance" : [500000,75000,250000,30000]
}

df = pd.DataFrame(customer)
print(df.shape)
print(df.columns)
print(df.dtypes)
print(df.info())