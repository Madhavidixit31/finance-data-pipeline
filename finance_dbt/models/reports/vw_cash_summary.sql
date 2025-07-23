-- models/reports/vw_cash_summary.sql

SELECT
    COUNT(*) FILTER (WHERE status = 'Paid') AS paid_invoices,
    COUNT(*) FILTER (WHERE status = 'Unpaid') AS unpaid_invoices
FROM {{ ref('stg_invoices') }}
