FROM python:3.10-slim

RUN apt-get update && apt-get install -y \
    wget \
    curl \
    && rm -rf /var/lib/apt/lists/*

RUN wget https://github.com/qdrant/qdrant/releases/download/v1.7.3/qdrant-x86_64-unknown-linux-gnu.tar.gz \
    && tar -xvf qdrant-x86_64-unknown-linux-gnu.tar.gz \
    && mv qdrant /usr/local/bin/qdrant \
    && chmod +x /usr/local/bin/qdrant

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 10000

CMD ["bash", "start_all.sh"]