#!/bin/bash

echo "Setting up kaggle API"

python3 -m pip install --upgrade pip
python3 -m pip install kaggle

mkdir ~/.kaggle
mv kaggle.json ~/.kaggle
chmod 600 ~/.kaggle/kaggle.json

kaggle datasets download tsiaras/uk-road-safety-accidents-and-vehicles
unzip uk-road-safety-accidents-and-vehicles.zip
rm -r uk-road-safety-accidents-and-vehicles.zip

kaggle datasets download tsiaras/predicting-profitable-customer-segments
unzip predicting-profitable-customer-segments.zip
rm -r predicting-profitable-customer-segments.zip

python3 -m pip install django
python3 -m pip install psycopg2


docker pull postgres
mkdir ./data/

docker run -d --name traffic -e POSTGRES_PASSWORD=n5pVTk2u -v data:/var/lib/postgresql/data -p 5432:5432 postgres
docker ps
docker exec -it traffic bash

# psql -h localhost -U postgres
psql postgres

CREATE ROLE masteruser WITH LOGIN PASSWORD 'n5pVTk2u';
ALTER USER masteruser CREATEDB;
CREATE DATABASE road_safety;

GRANT ALL PRIVILEGES ON DATABASE road_safety TO masteruser;

python3 manage.py inspectdb > ./traffic/models/models.py