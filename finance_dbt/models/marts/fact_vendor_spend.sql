-- models/marts/fact_vendor_spend.sql

SELECT
    vendor_name,
    SUM(CASE WHEN transaction_type = 'debit' THEN amount ELSE 0 END) AS total_spent
FROM {{ ref('stg_transactions') }}
GROUP BY vendor_name
ORDER BY total_spent DESC
