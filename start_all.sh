#!/usr/bin/env bash

echo "Starting Qdrant..."
qdrant &

echo "Starting FastAPI..."
uvicorn app.main:app --host 0.0.0.0 --port 10000