#!/bin/bash

echo "🚀 Đang khởi động N8nRagVN..."

# Kích hoạt môi trường ảo nếu có
# source venv/bin/activate

# Chạy FastAPI
uvicorn main:app --reload --host 0.0.0.0 --port 8000
