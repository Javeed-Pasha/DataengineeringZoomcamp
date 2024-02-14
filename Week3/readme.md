
#SETUP:

Maze Pipeline used to load green taxi data for 2022 . 

###Create an external table using the Green Taxi Trip Records Data for 2022.

    CREATE OR REPLACE EXTERNAL TABLE `forward-ace-411913.zoomcamp_bigquery.external_green_taxidata`
    OPTIONS (
      format = 'parquet',
      uris = [ 'gs://zoomcamp_b/nyc_taxi_data/66705163eaeb455cac02adbbc0d7e0e2-0.parquet']
    );

###Create a table in BQ using the Green Taxi Trip Records for 2022 (do not partition or cluster this table).

    CREATE OR REPLACE TABLE forward-ace-411913.zoomcamp_bigquery.green_taxidata_non_partitoned AS
    SELECT * FROM forward-ace-411913.zoomcamp_bigquery.external_green_taxidata;


Question 1: What is count of records for the 2022 Green Taxi Data??

    SELECT count( 1) FROM `forward-ace-411913.zoomcamp_bigquery.external_green_taxidata` 


Question2 : Write a query to count the distinct number of PULocationIDs for the entire dataset on both the tables.
What is the estimated amount of data that will be read when this query is executed on the External Table and the Table?
    
    SELECT count( distinct PULocationID )   from `forward-ace-411913.zoomcamp_bigquery.external_green_taxidata`;
    SELECT count( distinct PULocationID )   from  forward-ace-411913.zoomcamp_bigquery.green_taxidata_non_partitoned;


Question 3. How many records have a fare_amount of 0?

    SELECT count( 1 )   from  forward-ace-411913.zoomcamp_bigquery.green_taxidata_non_partitoned where fare_amount=0

    
