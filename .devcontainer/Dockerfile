# syntax=docker/dockerfile:1
FROM python:3.12-slim

# Install system packages for Tk / turtle and other tools
RUN apt-get update && \
    apt-get install -y --no-install-recommends python3-tk tk-dev xvfb git curl fonts-dejavu && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# (Optional) Pre-install Python deps here if you add a requirements.txt:
# COPY requirements.txt /tmp/requirements.txt
# RUN pip install --no-cache-dir -r /tmp/requirements.txt

WORKDIR /workspaces/Programming-Class-Project