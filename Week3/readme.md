
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

Answer :
    SELECT count( 1) FROM `forward-ace-411913.zoomcamp_bigquery.external_green_taxidata` 


Question2 : Write a query to count the distinct number of PULocationIDs for the entire dataset on both the tables.
What is the estimated amount of data that will be read when this query is executed on the External Table and the Table?

 Answer :   
    SELECT count( distinct PULocationID )   from `forward-ace-411913.zoomcamp_bigquery.external_green_taxidata`;
    SELECT count( distinct PULocationID )   from  forward-ace-411913.zoomcamp_bigquery.green_taxidata_non_partitoned;


Question 3. How many records have a fare_amount of 0?

Answer :
    SELECT count( 1 )   from  forward-ace-411913.zoomcamp_bigquery.green_taxidata_non_partitoned where fare_amount=0

Question 4 : What is the best strategy to make an optimized table in Big Query if your query will always order the results by PUlocationID and filter based on lpep_pickup_datetime? (Create a new table with this strategy)

    Answer : I have created an additional date column in data ingetion   called lpep_pickup_date  from lpep_pickup_datetime column.
            
            CREATE OR REPLACE TABLE forward-ace-411913.zoomcamp_bigquery.green_taxidata_partitoned 
            partition by    lpep_pickup_date
            cluster by  PULocationID AS
            SELECT * FROM forward-ace-411913.zoomcamp_bigquery.external_green_taxidata;


Question 5 . Write a query to retrieve the distinct PULocationID between lpep_pickup_datetime 06/01/2022 and 06/30/2022 (inclusive)
Use the materialized table you created earlier in your from clause and note the estimated bytes. Now change the table in the from clause to the partitioned table you created for question 4 and note the estimated bytes processed. What are these values?

Answer:
            SELECT COUNT (distinct PULocationID ) FROM forward-ace-411913.zoomcamp_bigquery.green_taxidata_partitoned 
            WHERE lpep_pickup_date BETWEEN '2022-06-01' AND '2022-06-30' 
            
            SELECT COUNT (distinct PULocationID ) FROM forward-ace-411913.zoomcamp_bigquery.green_taxidata_non_partitoned 
            WHERE lpep_pickup_date BETWEEN '2022-06-01' AND '2022-06-30' 


