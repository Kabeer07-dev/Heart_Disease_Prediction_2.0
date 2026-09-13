#!/bin/sh

uvicorn app:app --host 0.0.0.0 --port 8000 &

streamlit run streamlit_app/app.py \
    --server.address=0.0.0.0 \
    --server.port=8501