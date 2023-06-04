# use base image of python and add all the data in the present folder and run the main.py file on container start

FROM python:3.8-slim-buster

LABEL maintainer="Salil Gautam <salil.gtm@gmail.com>"
LABEL version="1.0"
LABEL description="GitHub CoPilot powered weather command line tool."

COPY ./src /workspace
COPY ./city_data /workspace
COPY requirements.txt /workspace

WORKDIR /workspace

RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT [ "python", "main.py" ]
