with raw_hosts AS (
    SELECT * FROM `fictional-lab-dev`.`airbnb`.`raw_hosts`
)
SELECT 
    id as host_id,
    name as host_name,
    IS_SUPERHOST,
    created_at,
    updated_at
FROM raw_hosts