FROM python:3.10-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install system dependencies for Chromium (and some extras)
RUN apt-get update && apt-get install -y \
    wget gnupg ca-certificates \
    fonts-liberation \
    libasound2 libatk1.0-0 libatk-bridge2.0-0 libcups2 libdbus-1-3 libdrm2 libgbm1 \
    libgtk-3-0 libnspr4 libnss3 libx11-xcb1 libx11-6 libxcomposite1 libxdamage1 \
    libxext6 libxfixes3 libxrandr2 libxrender1 libxshmfence1 libxss1 libxtst6 \
    libpango-1.0-0 libegl1 libglib2.0-0 libfontconfig1 libfreetype6 libpng16-16 \
    libicu[version appropriate] \
    && rm -rf /var/lib/apt/lists/*

# Install Playwright browsers + dependencies
RUN playwright install --with-deps chromium

COPY . .

EXPOSE 3000
CMD ["python", "koyeb_start.py"]
