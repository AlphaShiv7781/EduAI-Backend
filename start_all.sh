#!/usr/bin/env bash

echo "Starting Qdrant..."
qdrant &

echo "Waiting for Qdrant..."
sleep 8

echo "Starting FastAPI..."
uvicorn app.main:app --host 0.0.0.0 --port 10000