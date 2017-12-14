#!/bin/sh

gunicorn \
	-b 0.0.0.0:5000 \
	--worker-class gthread \
	--threads 5 \
	--access-logfile - \
	app:app
