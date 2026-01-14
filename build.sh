


#!/usr/bin/env bash
set -o errexit

pip install --upgrade pip setuptools wheel

# FORZAR BINARIOS (esto arregla Pillow)
pip install -r requirements.txt --prefer-binary

python manage.py collectstatic --noinput
python manage.py migrate
