# Dockerfile
# Change FROM python:3.13.5-slim-buster to:
FROM python:3.9-slim-buster 

# Install build-essential and other necessary development libraries
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    libffi-dev \
    libssl-dev \
    pkg-config \
    python3-dev \
    && \
    rm -rf /var/lib/apt/lists/* # Clean up apt cache

# Set the working directory in the container
WORKDIR /app

# Copy requirements.txt and install dependencies first (for caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code
COPY . .

# Expose the port Streamlit will run on
EXPOSE 8501

# Command to run your Streamlit application
CMD ["streamlit", "run", "app.py", "--server.port", "8501", "--server.enableCORS", "false", "--server.headless", "true"]
