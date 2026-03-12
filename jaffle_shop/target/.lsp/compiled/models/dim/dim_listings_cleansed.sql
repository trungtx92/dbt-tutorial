
WITH src_listings AS (
    SELECT *
    FROM `fictional-lab-dev`.`airbnb`.`src_listings`
)
SELECT
    listing_id,
    listing_name,
    room_type,
    CASE
        WHEN minimum_nights = 0 THEN 1
        ELSE minimum_nights
    END AS minimum_nights,
    host_id,
    CAST(REPLACE(price_str, '$', '') AS FLOAT64) AS price,
    created_at,
    updated_at
FROM src_listings