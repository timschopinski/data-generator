#!/bin/bash
cd $(dirname "${BASH_SOURCE[0]}")/app

rm db.sqlite3

rm -rf data/migrations/

python manage.py makemigrations

python manage.py migrate
