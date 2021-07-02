## traffic-accidents

This repository leverages the Kaggle API, to extract two datasets: Accident_Information.csv and Vehicle_Information.csv.

The most recent accidents we have vehicle data for into a Postgres database along with the dates these occurred, day of the week, severity index, driver home area, age bands, vehicle age and journey purpose. The goal is to be able to pull data from Kaggle and upload it in an input table in the Postgres database. Furthermore, input tables are then used to create fact tables with a mock ETL process built with Python Django commands. The Django framework also offers model management and to provide templates where data visualisations can be output. The latter are done in ChartJs.

###  Choices of Technology

The repository uses the following tech stack:

* Docker: Docker enables to run images in a container. This project contains: 
  * Dockerfile which defines the application’s image content via one build command that configures the image. This Dockerfile starts with a Python 3 parent image. A new code directory is added and all dependencies are installed via pip from the `requirements.txt` file. Furthermore, the kaggle API is installed and `kaggle.json` file is copied over to the image. From then on, the Dockerfile pulls the appropriate datasets, decompresses their contents and copies the extracted CSV files into the `traffic_accidents/traffic/data` folder.
  * docker-compose file (.yml) describes the services compose the application, being these a web server and database. The compose file also describes the Docker images and how they link together, as well as the volumes mounted into the containers. Finally, it describes the exposed port for the web server. The file defines three services (`db`, `init` and `web`). The first service sets up the postgres database that is then used in the following services. The `init` service is used to initialise the database data, and the `web` service is used to run the Python Django server on the appropriate host and port.
* PostgreSQL: the database used within the Docker image is a postgres database as it is object-relational. The database is easy to install and can be managed with pgAdmin. It also integrates with ease in Jupyter notebooks, Flask or Python Django.
* Python: The parent image in the Dockerfile is in Python 3. Python is a very clear object-oriented programming language that is used in software development and scientific and numeric computing environments, within others. Python was the coding language of choice due to its easy syntax, error handling and programming tasks integration.
* Django: As Python is used for clean coding capabilities and analytical purposes, the Django web framework can enable a clean and pragmatic design for a website that can be booted very quickly in a virtual environment or an image. 
* SQL: Raw SQL scripts are used to mock an ETL process, in order to process data in the database. The `init` service uses pandas to add the input data in the database. The data in the fact layer is processed via the SQL queries that are located in the `traffic_accidents/traffic/queries`, more specifically, `traffic_accidents/traffic/queries/accident_information.sql`. The rest of the queries within the folder are used to aggregate data that is then passed on to the Django template in JSON format.
* ChartJS: this is a simple data visualization API that can be integrated easily within JavaScript. It uses data structures that are easy to create and parse in Python and Django modules, such as JSON or object arrays.


### Pre-Requisites

Download or clone the [GitHub repository](https://github.com/alexmartincolville/traffic-accidents) to a directory of your preference.

The project leverages the Kaggle Python API to be able to obtain data. In order to so, a Kaggle account should be owned by the user in order to access the datasets.
Being that said, you should download your kaggle token via the Kaggle website (*kaggle.json file*) and place it in the project root directory.
This will use your Kaggle credentials to be able to download the data.

You will also need to have [Docker](https://www.docker.com/get-started) installed.

From here onwards, the process is fairly automated, and you should follow the usage section to be able to emulate the ETL process and start visualising the insights given from the data.

### Usage

The docker-compose file should leverage the postgres and application images. It also creates a dependency schema, where the init service (which initialises the data) depends on the database being in place. 
Build the Docker compose file:

`docker-compose build`

Start the postgres database service (we can detach this with -d):

`docker-compose up -d db`

On the first invocation of `docker-compose up` the `data` volume will be created. The same volume will be reused on following invocations.
Initialise the Python image with the Django website. This can also be detached, although we can then see the progress of the database tables being created and populated.

`docker-compose up init`

Run the Django server once the previous step has finished.

`docker-compose up -d web`

Booting up the Django site with the *runserver* command should initialise the website and show the data insights.
You are now be able to see the django site on your browser hosted in localhost:

`https://127.0.0.1:8000`

The data will be queried automatically as the image will start up a Django website which uses the queries in the *traffic/queries/* folder.
Data quality could be ensured by the input to fact process, which acts like an ETL taking into account the latest two years of data in which *Accident_Index* is in both datasets, so data is actually insightful for both datasets.

Your expected output should be a browser-based dashboard, where 4 different charts will appear.

If you wish to stop de web server, you can do so with the following command:

`docker-compose stop traffic.web`

It can also be restart with:

`docker-compose start traffic.web`


### Data Insights

The Dashboard (or Django website) shows four differents charts. These four charts stand for, from top left to bottom right:
* Percentage of accidents by driver age band;
* Percentage of accidents by age of vehicle;
* Total accidents by day of the week;
* Percentage of accidents by their severity.

Description of the data insights is provided at the bottom of each chart.

### Tests

A database connectivity test can be found in the `traffic_accidents/traffic/tests` folder. If the connection is successful, the test will pass.

Data tests are performed via the Django Framework. There are three tests in the `traffic_accidents/traffic/tests` folder, which check for each table in the data whether they are populated or not.
If the input tables are not populated, it would mean that the process that extracts data from Kaggle is not adding the data to the database, i.e. error in the Kaggle API or extracted CSVs are empty. If the input table already exists in the database, the pandas `to_sql` function will fail to update the table, as it should already be populated.

If the fact table is empty, it would mean that the Django command experienced an issue when pulling the data from the input layer (the pandas DataFrame may thus be empty). Also, in this step, if the table is already existing (the `init` image has already been ran), the pandas `to_sql` function will replace the table with the data in the DataFrame.

Tests can be triggered by opening up a bash CLI in the image with the following commmand:

`docker exec -it traffic.web bash`

And running the Django tests from the `traffic_accidents/` directory:

`python manage.py test`


### Contributions

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
Please make sure to update tests as appropriate.