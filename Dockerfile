FROM python:3.10-slim-buster

WORKDIR /app
COPY . /app

# Install awscli using pip
RUN pip install --no-cache-dir awscli

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python3", "app.py"]
