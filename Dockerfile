FROM python:3.10-slim

# -------------------------
# System dependencies
# -------------------------
RUN apt-get update && apt-get install -y \
    wget \
    curl \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# -------------------------
# Install Qdrant (MATCH client version)
# -------------------------
RUN wget https://github.com/qdrant/qdrant/releases/download/v1.16.2/qdrant-x86_64-unknown-linux-gnu.tar.gz \
    && tar -xvf qdrant-x86_64-unknown-linux-gnu.tar.gz \
    && mv qdrant /usr/local/bin/qdrant \
    && chmod +x /usr/local/bin/qdrant \
    && rm qdrant-x86_64-unknown-linux-gnu.tar.gz

# -------------------------
# App setup
# -------------------------
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# -------------------------
# Render expects one exposed port
# -------------------------
EXPOSE 10000

# -------------------------
# Start Qdrant + FastAPI
# -------------------------
CMD ["bash", "start_all.sh"]