# Python 3.10 slim imajını kullan
FROM python:3.10-slim

# Sistem kütüphanelerini yükleyin
RUN apt-get update && \
    apt-get install -y libgl1-mesa-glx libglib2.0-0 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN apt-get clean && rm -rf /var/lib/apt/lists/*


# Çalışma dizinini ayarlayın
WORKDIR /app

# Gereksinim dosyasını kopyalayın
COPY requirements.txt .

# Python bağımlılıklarını yükleyin
RUN pip install --no-cache-dir -r requirements.txt

# Uygulama dosyalarını kopyalayın
COPY app.py .
COPY apps/templates ./apps/templates
COPY static/uploads ./static/uploads
COPY Procfile .
COPY best.pt .
COPY runtime.txt .


# Uygulamayı başlatma komutu
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]
