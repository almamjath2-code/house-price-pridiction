# Base image
FROM python:3.11

# Work directory
WORKDIR /app

# Copy files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run app (FastAPI example)
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]

#docker build -t house-api .in temimnal this also use to rebuild 
#next run this docker run -p 8000:8000 house-api