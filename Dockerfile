# Use slim image to reduce size
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install required system packages (optional, if scipy or sklearn need it)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy only requirements first to leverage Docker caching
COPY app/requirements.txt ./requirements.txt

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy rest of the app
COPY app/ ./app/
COPY index.html .
COPY start.sh .
RUN chmod +x start.sh

# Expose the port expected by Render
EXPOSE 8000

# Default command
CMD ["./start.sh"]
