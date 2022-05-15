#!/usr/bin/env bash

if [ "$APP_ENV" == "dev" ]; then
	python local.py
else
	mkdir -p /var/log/gunicorn
	touch /var/log/gunicorn/error.log
	touch /var/log/gunicorn/access.log
	tail -fn 20 /var/log/gunicorn/*.log &

	gunicorn -c config/gunicorn.py "app:create_app()"
fi