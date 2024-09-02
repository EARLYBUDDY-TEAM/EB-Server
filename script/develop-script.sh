#!/bin/bash
PORT=8001

cd eb_fast_api/
python env/sources/env.py $PORT
uvicorn main:app --host 0.0.0.0 --port $PORT