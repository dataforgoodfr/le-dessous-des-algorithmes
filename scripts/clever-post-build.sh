#!/usr/bin/env bash
# Clever Cloud CC_POST_BUILD_HOOK: build React, then Django migrate/static.
set -euo pipefail

cd frontend
npm ci --include=dev
npm run build
cd ..

uv run python manage.py migrate --noinput
uv run python manage.py collectstatic --noinput
