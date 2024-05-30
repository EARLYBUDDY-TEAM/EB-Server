FROM python:3.12.3-slim

WORKDIR /api
COPY api .

RUN pip install -e .
RUN pip install -r requirements.txt

ENTRYPOINT ["python", "eb_fast_api/main.py"]