#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    CREATE ROLE masteruser WITH LOGIN PASSWORD 'n5pVTk2u';
    ALTER USER masteruser CREATEDB;
    CREATE SCHEMA input;
    CREATE SCHEMA dwh;
EOSQL