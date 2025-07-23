# Financial Business Data Pipeline

This project simulates a real world financial data pipeline for a small business. It uses PostgreSQL for storage, dbt for data modeling and Metabase for reporting.

---

## Pipeline Overview

1. **Data Generation**: Python was used to generate `transactions.csv` and `invoices.csv` for ~6 months of activity.
2. **Database**: Data is loaded into a PostgreSQL database in raw form (`source_transactions` and `source_invoices`).
3. **dbt Project**:
   - `staging/`: cleans and standardizes raw data
   - `marts/`: builds analytical tables like `fact_cash_position` and `fact_vendor_spend`
   - `reports/`: creates reporting views like `vw_cash_summary`
4. **Testing**: Basic dbt tests validate the structure, value constraints, and null handling.
5. **Metabase**: Connects to PostgreSQL to build 3 key dashboard charts.

---

## Tech Stack

- **PostgreSQL** – raw data storage (transactions + invoices)
- **dbt** – data transformation and model management
- **Metabase** – interactive dashboarding
- **Python (Pandas)** – data generation

---

## Dataset

Two datasets (6 months of activity):

### `transactions.csv`
| Column        | Description               |
|---------------|---------------------------|
| `date`        | Transaction date          |
| `type`        | Credit or Debit           |
| `vendor_name` | Vendor name               |
| `amount`      | Transaction amount        |
| `balance`     | Running account balance   |

### `invoices.csv`
| Column        | Description               |
|---------------|---------------------------|
| `invoice_date`| Date issued               |
| `due_date`    | Due date for payment      |
| `vendor_name` | Vendor name               |
| `invoice_amount` | Amount billed          |
| `status`      | Paid or Unpaid            |

---

## dbt Models

### Staging (`models/staging`)
- `stg_transactions.sql`
- `stg_invoices.sql`

### Marts (`models/marts`)
- `fact_cash_position.sql`: tracks daily balance
- `fact_vendor_spend.sql`: total spend by vendor

### Reporting (`models/reports`)
- `vw_cash_summary.sql`: invoice status summary

---

## dbt Tests

Basic data quality tests were added to ensure model integrity.

### Tests applied:

#### `stg_transactions.sql`
- `transaction_date`: `not null`
- `vendor_name`: `not null`

#### `stg_invoices.sql`
- `invoice_date`: `not null`
- `status`: `accepted_values` → ['Paid', 'Unpaid']

All tests are defined in `src_finance.yml`.

To run the tests:

dbt test

---

## Dashboard (Metabase)

Built 3 key visuals:
- **Line Chart**: Daily ending cash balance
- **Bar Chart**: Top vendors by spend
- **Pie Chart**: Paid vs. unpaid invoices

---

## Assumptions

- Vendor names are consistent across tables
- Balance in `transactions` reflects real time changes
- No partial invoice payments (Paid/Unpaid only)
- `transaction_type` is either `'credit'` or `'debit'`
- `invoices.status` is either `'Paid'` or `'Unpaid'`

---

## Future Extensions

- Add a `customers` table and track revenue by customer
- Schedule the pipeline with Airflow or dbt Cloud
- Add alerts for low cash days or overdue invoices
- Integrate with real accounting software (QuickBooks, Stripe APIs)

---

## Repo Structure

finance_pipeline/
├── data/
│   ├── transactions.csv
│   └── invoices.csv
├── finance_dbt/
│   ├── dbt_project.yml
│   ├── README.md        
│   ├── models/
│   │   ├── staging/
│   │   │   ├── stg_transactions.sql
│   │   │   ├── stg_invoices.sql
│   │   │   └── stg_finance_tests.yml
│   │   ├── marts/
│   │   │   ├── fact_cash_position.sql
│   │   │   └── fact_vendor_spend.sql
│   │   └── reports/
│   │       └── vw_cash_summary.sql
