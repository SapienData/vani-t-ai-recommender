# Use Python 3.11 slim
FROM python:3.11-slim

WORKDIR /app

# Install backend dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy everything including React build
COPY . .

# Expose port
EXPOSE 5000

# Run Flask
CMD ["python", "app.py"]