# syntax=docker/dockerfile:1

FROM python:3

ENV PYTHONUNBUFFERED=1
WORKDIR /traffic_accidents
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

RUN mkdir ~/.kaggle
RUN mv kaggle.json ~/.kaggle
RUN chmod 600 ~/.kaggle/kaggle.json

RUN kaggle datasets download tsiaras/uk-road-safety-accidents-and-vehicles
RUN unzip uk-road-safety-accidents-and-vehicles.zip
RUN rm -r uk-road-safety-accidents-and-vehicles.zip

RUN kaggle datasets download tsiaras/predicting-profitable-customer-segments
RUN unzip predicting-profitable-customer-segments.zip
RUN rm -r predicting-profitable-customer-segments.zip

COPY . .