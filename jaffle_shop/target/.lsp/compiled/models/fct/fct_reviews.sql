
WITH src_reviews AS (
    SELECT *
    FROM `fictional-lab-dev`.`airbnb`.`src_reviews`
)
SELECT 
    listing_id,
    review_date,
    reviewer_name,
    review_text,
    review_sentiment
FROM src_reviews
WHERE review_text IS NOT NULL

    AND review_date >= (SELECT MAX(review_date) FROM `fictional-lab-dev`.`airbnb`.`fct_reviews`)
