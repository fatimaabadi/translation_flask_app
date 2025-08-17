# Use official Python image
FROM python:3.11-slim

# Set working directory in the container
WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project files into the container
COPY . .

# Expose the port Flask runs on
EXPOSE 5000

# Run the app
CMD ["python", "app.py"]
