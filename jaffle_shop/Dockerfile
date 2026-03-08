FROM ghcr.io/dbt-labs/dbt-bigquery:1.7.0
WORKDIR /usr/app
COPY . .
ENV DBT_PROFILES_DIR=/usr/app
RUN dbt deps
ENTRYPOINT ["dbt"]
CMD ["run"]