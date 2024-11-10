#!/bin/bash

# Exit script on any error
set -e

# Define variables
DOMAIN="dkrrs.net"
CERT_DIR="./certs"
WEBROOT_DIR="./certbot/www"

# Create necessary directories if they don't exist
mkdir -p "$CERT_DIR"
mkdir -p "$WEBROOT_DIR"

echo "Starting Nginx container to serve ACME challenge..."
# Start Nginx in detached mode (needed for HTTP challenge)
docker-compose up -d nginx

echo "Generating SSL certificate for $DOMAIN using Let's Encrypt..."
# Run Certbot to obtain the SSL certificate
docker-compose run certbot certonly --webroot -w /var/www/certbot --email cemehel@gmail.com -d "$DOMAIN"

# Check if the certificate was successfully generated
if [ -f "$CERT_DIR/live/$DOMAIN/fullchain.pem" ]; then
    echo "SSL certificate successfully generated for $DOMAIN."
else
    echo "Failed to generate SSL certificate for $DOMAIN."
    exit 1
fi

echo "Restarting Nginx container to apply SSL configuration..."
# Restart Nginx to apply the SSL configuration
docker-compose restart nginx

echo "SSL setup completed successfully. Visit https://$DOMAIN to verify."
