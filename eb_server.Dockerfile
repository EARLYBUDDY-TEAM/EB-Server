FROM python:3.12.3-slim

WORKDIR /mycode
COPY . .

RUN pip install -e .
RUN pip install -r requirements.txt