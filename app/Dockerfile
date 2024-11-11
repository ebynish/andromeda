# app/Dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY app.py .

RUN pip install Flask psycopg2-binary

EXPOSE 5000

ENTRYPOINT ["/app/entrypoint.sh"]
CMD ["python", "app.py"]
