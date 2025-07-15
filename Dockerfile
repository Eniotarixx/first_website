# Base image  
FROM python:3.13.5-bookworm

# Work directory 
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY add.py .
COPY main.py .
COPY templates/ ./templates/
COPY static/ ./static

EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
