
  
    

    create or replace table `fictional-lab-dev`.`airbnb`.`dim_hosts_cleansed`
      
    
    

    
    OPTIONS()
    as (
      WITH src_hosts AS (
    SELECT *
    FROM `fictional-lab-dev`.`airbnb`.`src_hosts`
)

SELECT
    host_id,
    IFNULL(host_name, 'Anonymous') AS host_name,
    IS_SUPERHOST,
    created_at,
    updated_at
FROM src_hosts
    );
  