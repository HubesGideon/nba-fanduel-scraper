# Use an official lightweight Python image
FROM python:3.11-slim

# Install system dependencies needed for Playwright
RUN apt-get update && apt-get install -y \
    wget gnupg ca-certificates curl fonts-liberation libasound2 libatk-bridge2.0-0 libatk1.0-0 libcups2 \
    libdbus-1-3 libgdk-pixbuf2.0-0 libx11-xcb1 libxcomposite1 libxdamage1 libxrandr2 \
    libgbm1 libnss3 libpango-1.0-0 libpangocairo-1.0-0 libxss1 libxtst6 fonts-noto-color-emoji

# Install Python packages
RUN pip install --upgrade pip
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# 📢 📢 ADD THIS LINE TO INSTALL CHROMIUM
RUN playwright install chromium

# Copy app files
COPY . .

# Run app
CMD ["python", "fanduel_scraper.py"]
