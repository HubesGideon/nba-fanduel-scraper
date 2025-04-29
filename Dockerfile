FROM python:3.11-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    wget gnupg ca-certificates curl fonts-liberation libasound2 libatk-bridge2.0-0 libatk1.0-0 libcups2 \
    libdbus-1-3 libgdk-pixbuf2.0-0 libgtk-3-0 libx11-xcb1 libxcb1 libxcomposite1 libxdamage1 libxext6 \
    libxfixes3 libxrandr2 libgbm1 libpango-1.0-0 libpangocairo-1.0-0 libatk1.0-0 libcairo2 libnss3 libxss1 \
    libxtst6 libx11-6 libxkbcommon0 libxshmfence1 xvfb

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY . .

# Run your script
CMD ["python", "fanduel_scraper.py"]
