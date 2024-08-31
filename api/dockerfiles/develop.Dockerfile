# syntax = edrevo/dockerfile-plus

INCLUDE+ env.Dockerfile

WORKDIR /eb_fast_api
ENTRYPOINT ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001"]