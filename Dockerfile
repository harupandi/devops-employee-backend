FROM python:3.12-slim-trixie

WORKDIR /app

RUN apt-get update && \
    apt-get upgrade -y

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app ./app
COPY run.py .

EXPOSE 5000

CMD ["python", "run.py"]
