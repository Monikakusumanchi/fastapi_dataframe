# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the FastAPI and Uvicorn dependencies
RUN pip install --no-cache-dir -r requirements.txt --index-url=https://pypi.org/simple/

# Copy the FastAPI code and templates into the container
COPY . .

# Expose the FastAPI port
EXPOSE 8000

# Run the FastAPI application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
