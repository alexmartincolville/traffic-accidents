## traffic-accidents

This repository leverages the Kaggle API, to extract two datasets: Accident_Information.csv and Vehicle_Information.csv.

The most recent accidents we have vehicle data for into a Postgres database along with the dates
these occurred, day of the week, severity index, driver home area, age bands, vehicle age and journey
purpose.

How to run it:

First, you should download your kaggle token via the Kaggle website (*kaggle.json file*) and place it in your root directory.

The docker-compose file should leverage the postgres and application images, creating a simple ETL that add all data to an input schema and using this data to create a fact table that is added to the dwh shcema. 
Bbooting up the Django site with the *runserver* command should initialise the website and show the data insights.

`docker-compose up --build`

The data will be queried automatically as the image will start up a Django website which uses the queries in the *traffic/queries/* folder.
Data quality could be ensured by the input to fact process, which acts like an ETL taking into account the latest two years of data in which *Accident_Index* is in both datasets, so data is actually insightful for both datasets.