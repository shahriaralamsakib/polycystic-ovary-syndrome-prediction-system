# Use an official Python runtime as a parent image
FROM python:3.10-slim AS builder

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install system dependencies
RUN apt-get update \
    && apt-get install -y build-essential libpq-dev \
    && apt-get clean

# Create a working directory
WORKDIR /app

# Install Python dependencies in a virtual environment
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Copy the requirements file and install dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Copy the Django project code
COPY . /app/

# Use a second, smaller image for runtime
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PATH="/opt/venv/bin:$PATH"

# Copy the virtual environment from the builder stage
COPY --from=builder /opt/venv /opt/venv

# Create a working directory
WORKDIR /app

# Copy the application code from the builder stage
COPY --from=builder /app /app

# Expose the port the app runs on
EXPOSE 8000

# Collect static files (if needed)
RUN python /app/manage.py collectstatic --noinput

# Run the Django server
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "PCOS.wsgi:application"]
