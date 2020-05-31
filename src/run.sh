#!/bin/sh

app_debug="${app_debug:-0}"
set -eu

if [ "$app_debug" = "1" ]; then
	pipenv run tests
	FLASK_DEBUG=1 pipenv run flask run -h 0.0.0.0 -p 8000
else
	pipenv run gunicorn -b 0.0.0.0:8000 -w 1 -n cdocstore app:app
fi
