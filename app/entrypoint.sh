#!/bin/bash
# entrypoint.sh
echo "Waiting for PostgreSQL to start..."
while ! nc -z postgres-db 5432; do
  sleep 0.1
done
echo "PostgreSQL started successfully."

exec "$@"
