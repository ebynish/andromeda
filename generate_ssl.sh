#!/bin/bash

# Set domain names for which you want to generate SSL certificates
DOMAINS=("dkrrs.net")
WEBROOT_PATH="/var/www/certbot"
NGINX_CONF_DIR="/etc/nginx"

# Run Certbot to generate SSL certificates
docker-compose run --rm certbot certonly --webroot \
  --webroot-path="$WEBROOT_PATH" \
  --email cemehel@gmail.com \
  --agree-tos \
  --no-eff-email \
  "${DOMAINS[@]/#/--domains=}"

# Reload Nginx to apply the newly generated certificates
docker-compose exec nginx nginx -s reload

# Print success message
echo "SSL certificates generated and Nginx reloaded successfully!"
