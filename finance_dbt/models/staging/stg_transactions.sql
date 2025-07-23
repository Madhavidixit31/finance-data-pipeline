-- models/staging/stg_transactions.sql

SELECT
    date AS transaction_date,
    LOWER(type) AS transaction_type,
    vendor_name,
    amount,
    balance
FROM {{ source('public', 'source_transactions') }}
