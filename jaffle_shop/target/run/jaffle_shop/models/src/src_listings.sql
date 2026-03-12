

  create or replace view `fictional-lab-dev`.`airbnb`.`src_listings`
  OPTIONS()
  as with raw_listings AS (
    SELECT * FROM `fictional-lab-dev`.`airbnb`.`raw_listings`
)
SELECT 
    id as listing_id,
    name AS listing_name,
    listing_url,
    room_type,
    minimum_nights,
    host_id,
    price AS price_str,
    created_at,
    updated_at
FROM raw_listings;

