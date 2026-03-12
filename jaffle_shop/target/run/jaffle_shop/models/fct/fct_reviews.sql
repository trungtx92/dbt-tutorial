-- back compat for old kwarg name
  
  
        
    

    

    merge into `fictional-lab-dev`.`airbnb`.`fct_reviews` as DBT_INTERNAL_DEST
        using (
        select
        * from `fictional-lab-dev`.`airbnb`.`fct_reviews__dbt_tmp`
        ) as DBT_INTERNAL_SOURCE
        on (FALSE)

    

    when not matched then insert
        (`listing_id`, `review_date`, `reviewer_name`, `review_text`, `review_sentiment`)
    values
        (`listing_id`, `review_date`, `reviewer_name`, `review_text`, `review_sentiment`)


    