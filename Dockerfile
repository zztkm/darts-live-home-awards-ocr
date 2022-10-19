FROM ubuntu:latest

RUN apt-get update && apt-get install -y tesseract-ocr
RUN apt-get install -y python3 python3-pip

RUN mkdir /home/work
COPY requirements.txt /home/work/requirements.txt
WORKDIR /home/work

RUN pip3 install -r requirements.txt
