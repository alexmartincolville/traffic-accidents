# syntax=docker/dockerfile:1

FROM python:3

WORKDIR /
COPY requirements.txt requirements.txt
RUN pip install kaggle
RUN pip install -r requirements.txt

RUN mkdir /root/.kaggle
COPY kaggle.json /root/.kaggle
RUN chmod 600 /root/.kaggle/kaggle.json

RUN kaggle datasets download tsiaras/uk-road-safety-accidents-and-vehicles
RUN unzip uk-road-safety-accidents-and-vehicles.zip
RUN rm -r uk-road-safety-accidents-and-vehicles.zip

RUN kaggle datasets download tsiaras/predicting-profitable-customer-segments
RUN unzip predicting-profitable-customer-segments.zip
RUN rm -r predicting-profitable-customer-segments.zip

COPY init-user-db.sh /docker-entrypoint-initdb.d
COPY . .