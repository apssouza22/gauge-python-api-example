FROM python:3.7

RUN apt-get update
RUN apt-get -y install sudo
RUN apt-get install apt-transport-https -y

#Install gauge
RUN curl -SsL https://downloads.gauge.org/stable | sh
RUN gauge install python
RUN pip install --upgrade pip
RUN pip install colorama
RUN pip install getgauge
RUN gauge -v
ENV PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION=python
RUN gauge -v
WORKDIR /gauge

# Copy go.mod and go.sum files and download modules
# Note: prevents layer from being rebuilt unless go.mod and/or go.sum change
# Ref: HSS
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .
