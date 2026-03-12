

  create or replace view `fictional-lab-dev`.`airbnb`.`src_reviews`
  OPTIONS()
  as with raw_reviews AS (
    SELECT * FROM `fictional-lab-dev`.`airbnb`.`raw_reviews`
)
SELECT 
    listing_id,
    date as review_date,
    reviewer_name,
    comments as review_text,
    sentiment as review_sentiment
FROM raw_reviews;

