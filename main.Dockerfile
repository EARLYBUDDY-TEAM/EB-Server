FROM python:3.12.3-slim

COPY . .

RUN pip install -e .
RUN pip install -r requirements.txt

ENTRYPOINT ["sh", "./script/main-script.sh", "8000"]