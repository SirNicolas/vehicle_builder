#! /usr/bin/env bash

# Run migrations
alembic upgrade head

python /app/app/main.py