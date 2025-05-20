# -Dockerize-as-DevOps
 Dockerize and prepare for cloud deployment
Creating a Dockerfile for a FastAPI application using PowerShell involves a few steps. Below is a step-by-step guide, including how you can do it in PowerShell on Windows, along with a sample Dockerfile. 

Shape 

✅ Step-by-Step Instructions 

🧱 Step 1: Set Up Your FastAPI Application 

Let's assume your project structure looks like this: 

fastapi-app/ 

│ 

├── app/ 

│   ├── main.py 

│   └── __init__.py 

├── requirements.txt 

└── Dockerfile 

main.py contains your FastAPI app. 

main.py example: 

from fastapi import FastAPI 

 

app = FastAPI() 

 

@app.get("/") 

def read_root(): 

    return {"message": "Hello from FastAPI"} 

Shape 

📦 Step 2: Create requirements.txt 

You can generate it with PowerShell: 

pip freeze > requirements.txt 

Or just create it manually: 

requirements.txt: 

fastapi 

uvicorn[standard] 

Shape 

🐳 Step 3: Write the Dockerfile 

PowerShell Command to Create Dockerfile: 

New-Item -Path . -Name "Dockerfile" -ItemType "File" 

Then open it in Notepad: 

notepad Dockerfile 

Paste the following content into the Dockerfile: 

# Use official Python base image 

FROM python:3.11-slim 

 

# Set the working directory 

WORKDIR /app 

 

# Copy requirements and install dependencies 

COPY requirements.txt . 

RUN pip install --no-cache-dir -r requirements.txt 

 

# Copy application code 

COPY ./app ./app 

 

# Set environment variable (optional) 

ENV PYTHONUNBUFFERED=1 

 

# Run the application 

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"] 

Shape 

🔧 Step 4: Build Docker Image 

In PowerShell: 

docker build -t fastapi-app . 

Shape 

🚀 Step 5: Run the Container 

docker run -d -p 8000:8000 fastapi-app 

Visit: http://localhost:8000 

Shape 

🧪 Optional: Check Logs 

docker logs <container_id> 

Get container ID: 

docker ps 

Shape 

If you'd like, I can generate the files for you or help you containerize a more complex FastAPI app too. 

 
