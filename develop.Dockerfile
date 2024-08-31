FROM python:3.12.3-slim

COPY . .

RUN pip install -e .
RUN pip install -r requirements.txt

WORKDIR /eb_fast_api
ENTRYPOINT ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001"]