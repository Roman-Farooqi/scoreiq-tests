# 1. Base Image
FROM python:3.9-slim

# 2. Update Linux packages aur Chrome & WebDriver install karein (Fixed for Debian)
RUN apt-get update && apt-get install -y \
    wget \
    gnupg \
    unzip \
    chromium \
    chromium-driver \
    && rm -rf /var/lib/apt/lists/*

# 3. Container ke andar ek folder banayein
WORKDIR /app

# 4. Apne laptop se requirements copy karein
COPY requirements.txt .

# 5. Selenium install karein
RUN pip install --no-cache-dir -r requirements.txt

# 6. Apni asli test file copy karein
COPY test_scoreiq.py .

# 7. Test file ko chala do
CMD ["python", "test_scoreiq.py"]