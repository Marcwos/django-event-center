#!/usr/bin/env bash
# Salir inmediatamente si ocurre un error
set -o errexit  

# Instalar dependencias
pip install --upgrade pip
pip install -r requirements.txt

# Recolección de archivos estáticos (sin interacción)
python manage.py collectstatic --no-input  

# Aplicar migraciones a la base de datos
python manage.py migrate
