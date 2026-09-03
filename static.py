import pandas as pd
import numpy as np

data = {
    "transaction_id" : range(1001, 1031),
    "customer_id": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110,
                    111, 112, 113, 114, 115, 116, 117, 118, 119, 120,
                    121, 122, 123, 124, 125, 126, 127, 128, 129, 130],
    "age": [25, 34, 42, 29, 51, 37, 45, 31, 28, 56,
            39, 47, 26, 33, 41, 52, 36, 44, 30, 49,
            27, 38, 55, 32, 43, 35, 48, 29, 40, 53],
    "transaction_amount": [1200, 4500, 750, 12000, 3500, 8500, 2200, 15000, 1800, 6500,
                          3200, 9000, 1100, 4800, 7200, 13500, 2500, 5600, 1900, 8200,
                          3000, 11000, 1400, 6200, 4100, 9700, 1600, 5300, 2800, 12500],
    "processing_time_sec": [4.2, 5.1, 4.8, 7.2, 5.4, 6.1, 4.5, 8.2, 4.7, 6.8,
                            5.0, 6.4, 4.1, 5.3, 6.0, 7.5, 4.9, 5.8, 4.6, 6.7,
                            5.2, 7.0, 4.3, 6.2, 5.5, 6.5, 4.4, 5.7, 4.8, 7.3],
    "branch": ["Mumbai", "Pune", "Delhi", "Bangalore", "Mumbai", "Pune", "Delhi", "Bangalore", "Mumbai", "Pune",
               "Delhi", "Bangalore", "Mumbai", "Pune", "Delhi", "Bangalore", "Mumbai", "Pune", "Delhi", "Bangalore",
               "Mumbai", "Pune", "Delhi", "Bangalore", "Mumbai", "Pune", "Delhi", "Bangalore", "Mumbai", "Pune"],
    "channel": ["UPI", "Card", "UPI", "Card", "NetBanking", "UPI", "Card", "UPI", "NetBanking", "Card",
                "UPI", "Card", "UPI", "NetBanking", "Card", "UPI", "Card", "UPI", "NetBanking", "Card",
                "UPI", "Card", "UPI", "Card", "NetBanking", "UPI", "Card", "UPI", "NetBanking", "Card"],
    "status": ["Success", "Success", "Success", "Failed", "Success", "Success", "Failed", "Success", "Success", "Success",
               "Failed", "Success", "Success", "Success", "Failed", "Success", "Success", "Failed", "Success", "Success",
               "Success", "Failed", "Success", "Success", "Failed", "Success", "Success", "Failed", "Success", "Success"]
}

df = pd.DataFrame(data