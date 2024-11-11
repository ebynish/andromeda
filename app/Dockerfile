# app/Dockerfile
FROM python:3.11-slim

WORKDIR /app

# Install netcat-openbsd (alternative to netcat)
RUN apt-get update && apt-get install -y netcat-openbsd

COPY . /app
COPY entrypoint.sh /app/entrypoint.sh

RUN chmod +x /app/entrypoint.sh

RUN pip install Flask psycopg2-binary

EXPOSE 5000

ENTRYPOINT ["/app/entrypoint.sh"]
CMD ["python", "app.py"]
