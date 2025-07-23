-- models/staging/stg_invoices.sql

SELECT
    invoice_date,
    due_date,
    vendor_name,
    invoice_amount,
    status
FROM {{ source('public', 'source_invoices') }}
