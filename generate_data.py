import pandas as pd
import random
from faker import Faker
from datetime import timedelta

fake = Faker()
start_date = pd.to_datetime("2024-01-01")
end_date = pd.to_datetime("2024-06-30")
date_range = pd.date_range(start=start_date, end=end_date, freq='D')

# --- Transactions Table ---
vendors = ["Amazon", "Uber", "Starbucks", "Walmart", "Dropbox", "Zoom", "Stripe"]
transactions = []

balance = 10000  # initial balance

for date in date_range:
    for _ in range(random.randint(1, 3)):  # 1 to 3 transactions per day
        vendor = random.choice(vendors)
        txn_type = random.choice(["Credit", "Debit"])
        amount = round(random.uniform(20, 500), 2)

        if txn_type == "Debit":
            balance -= amount
        else:
            balance += amount

        transactions.append({
            "date": date.date(),
            "type": txn_type,
            "vendor_name": vendor,
            "amount": amount,
            "balance": round(balance, 2)
        })

df_txn = pd.DataFrame(transactions)
df_txn.to_csv("transactions.csv", index=False)

# --- Invoices Table ---
invoices = []
for _ in range(200):
    invoice_date = fake.date_between(start_date=start_date, end_date=end_date)
    due_date = invoice_date + timedelta(days=random.randint(15, 45))
    vendor = random.choice(vendors)
    invoice_amount = round(random.uniform(100, 1500), 2)
    status = random.choice(["Paid", "Unpaid"])

    invoices.append({
        "invoice_date": invoice_date,
        "due_date": due_date,
        "vendor_name": vendor,
        "invoice_amount": invoice_amount,
        "status": status
    })

df_invoice = pd.DataFrame(invoices)
df_invoice.to_csv("invoices.csv", index=False)

print("CSVs created: transactions.csv and invoices.csv")
