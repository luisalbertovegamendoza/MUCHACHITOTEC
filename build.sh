


#!/usr/bin/env bash
set -o errexit

pip install --upgrade pip setuptools wheel

# FORZAR BINARIOS (esto arregla Pillow)
pip install --only-binary=:all: Pillow==9.5.0
pip install -r requirements.txt --prefer-binary

python manage.py collectstatic --noinput
python manage.py migrate
