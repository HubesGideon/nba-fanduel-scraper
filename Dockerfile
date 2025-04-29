FROM python:3.11-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    wget gnupg ca-certificates curl fonts-liberation libasound2 libatk-bridge2.0-0 libatk1.0-0 libcups2 \
    libdbus-1-3 libgdk-pixbuf2.0-0 libnspr4 libnss3 libx11-xcb1 libxcomposite1 libxdamage1 libxrandr2 \
    libxss1 libxtst6 xdg-utils libgtk-3-0 libdrm2 libgbm1 libxshmfence1 xvfb

# Install Python packages
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ❗ ADD THIS LINE
RUN playwright install --with-deps

# Copy the rest of the code
COPY . .

# Command to run your script
CMD ["python", "fanduel_scraper.py"]
