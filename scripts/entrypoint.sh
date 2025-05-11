#!/bin/sh

# Espera a que la base de datos esté lista
echo "Esperando a la base de datos..."
/wait_for_db.sh

# Aplica migraciones automáticamente
echo "Aplicando migraciones..."
python manage.py migrate --noinput

# Ejecuta el servidor
echo "Iniciando el servidor Django..."
exec python manage.py runserver 0.0.0.0:8000
