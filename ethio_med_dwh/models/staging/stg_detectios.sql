{{
  config(
    materialized='view'
  )
}}

SELECT
    image_path,
    object AS detected_object,
    confidence,
    bbox
FROM {{ source('raw', 'raw_object_detections') }}