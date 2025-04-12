# ~/N8nRagVN/main.py

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import chromadb

app = FastAPI()

# Mount frontend
app.mount("/static", StaticFiles(directory="frontend"), name="static")

# Route để trả về giao diện chính
@app.get("/")
def read_index():
    return FileResponse("frontend/index.html")

# Init ChromaDB (cấu hình đơn giản)
@app.on_event("startup")
def startup_event():
    client = chromadb.Client()
    print("✅ ChromaDB client initialized")

# Test API
@app.get("/api/hello")
def hello():
    return {"message": "Hello from FastAPI + ChromaDB"}
