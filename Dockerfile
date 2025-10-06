# Use lightweight Python base
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy dependency file
COPY requirements.txt .

# Install system dependencies required for Chrome & Playwright
RUN apt-get update && apt-get install -y \
    wget gnupg ca-certificates \
    fonts-liberation \
    libasound2 libatk1.0-0 libatk-bridge2.0-0 libcups2 libdbus-1-3 libdrm2 libgbm1 \
    libgtk-3-0 libnspr4 libnss3 libx11-xcb1 libx11-6 libxcomposite1 libxdamage1 \
    libxext6 libxfixes3 libxrandr2 libxrender1 libxshmfence1 libxss1 libxtst6 \
    libpango-1.0-0 libegl1 libglib2.0-0 libfontconfig1 libfreetype6 libpng16-16 \
    libicu71 \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install Playwright and Chromium (if your app uses Playwright)
RUN pip install playwright && playwright install --with-deps chromium

# Copy application files
COPY . .

# Expose the app port (change if needed)
EXPOSE 7860

# Set timezone if required (optional)
ENV TZ=Africa/Lagos

# Start the app
CMD ["python", "koyeb_start.py"] 
