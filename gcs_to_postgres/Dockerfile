FROM python:3.11-slim
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libpq-dev \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*   # cleanup to keep image small
WORKDIR /usr/app
COPY . .
ENV DBT_PROFILES_DIR=/usr/app
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python3", "main.py"]