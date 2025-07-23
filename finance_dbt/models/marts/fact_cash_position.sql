-- models/marts/fact_cash_position.sql

SELECT
    transaction_date,
    MAX(balance) AS daily_ending_balance
FROM {{ ref('stg_transactions') }}
GROUP BY transaction_date
ORDER BY transaction_date
