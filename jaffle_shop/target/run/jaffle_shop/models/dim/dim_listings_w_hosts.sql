
  
    

    create or replace table `fictional-lab-dev`.`airbnb`.`dim_listings_w_hosts`
      
    
    

    
    OPTIONS()
    as (
      WITH l AS (
    SELECT * FROM `fictional-lab-dev`.`airbnb`.`dim_listings_cleansed`
),
h AS (
    SELECT * FROM `fictional-lab-dev`.`airbnb`.`dim_hosts_cleansed`
)
SELECT
    l.listing_id,
    l.listing_name,
    l.room_type,
    l.minimum_nights,
    l.price,
    l.host_id,
    h.host_name,
    h.is_superhost as host_is_superhost,
    l.created_at,
    GREATEST(l.updated_at, h.updated_at) AS updated_at
FROM l
LEFT JOIN h ON h.host_id = l.host_id
    );
  