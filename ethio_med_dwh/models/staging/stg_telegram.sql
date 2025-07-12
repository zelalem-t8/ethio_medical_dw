{{
  config(
    materialized='view'
  )
}}

SELECT
    date AS message_time,
    message,
    channel,
    phone_numbers,
    business_type
FROM {{ source('raw', 'raw_telegram_messages') }}