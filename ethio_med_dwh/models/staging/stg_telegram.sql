{{
  config(
    materialized='view'
  )
}}

SELECT
    -- Add a unique identifier - here are some options:
    
    -- Option 1: Use ROW_NUMBER() to create a synthetic ID
    ROW_NUMBER() OVER (ORDER BY date, channel) AS id,
    
    -- Option 2: If you have a natural unique key, use that instead
    -- some_unique_field AS id,
    
    date AS message_time,
    message,
    channel,
    phone_numbers,
    business_type
FROM {{ source('raw', 'raw_telegram_messages') }}