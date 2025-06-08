# main.py

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI from Docker!"}

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
