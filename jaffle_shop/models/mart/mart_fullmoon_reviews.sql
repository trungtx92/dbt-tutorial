{{
    config(
        materialized = "table"
    )
}}
WITH fct_reviews AS (
    SELECT *
    FROM {{ ref("fct_reviews") }}
),
full_moon_dates AS (
    SELECT *
    FROM {{ ref("seed_full_moon_dates") }}
)
SELECT 
    r.*, 
    CASE 
    WHEN fm.full_moon_date IS NULL THEN 'Not Full Moon' 
    ELSE 'Full Moon' END AS is_moon_review
FROM fct_reviews r
LEFT JOIN full_moon_dates fm
ON (DATE(r.review_date) = DATE_ADD(fm.full_moon_date, INTERVAL 1 DAY))