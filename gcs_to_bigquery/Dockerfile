FROM python:3.11-slim
WORKDIR /usr/app
COPY . .
ENV DBT_PROFILES_DIR=/usr/app
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python3", "main.py"]