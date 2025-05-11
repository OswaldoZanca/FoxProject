#!/bin/sh

echo "Esperando a que la base de datos esté disponible..."

while ! nc -z db 5432; do
  sleep 1
done

echo "Base de datos disponible, ejecutando comando: $@"
exec "$@"
