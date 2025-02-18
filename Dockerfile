# Use Python 3.9 slim image for a smaller footprint
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy requirements first to leverage Docker cache
COPY deepseek_demo/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY deepseek_demo/ .

# Expose port 8000 for FastAPI
EXPOSE 7777

# Command to run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "7777"]
