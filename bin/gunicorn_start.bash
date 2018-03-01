#!/usr/bin/env bash

NAME="macs_server"
DJANGODIR=/home/chris/projects/python/web/django/macs_server
SOCKFILE=$DJANGODIR/run/$NAME.sock
USER=www-data
GROUP=www-data
NUM_WORKERS=3
DJANGO_SETTINGS_MODULE=forge_macs.settings
DJANGO_WSGI_MODULE=forge_macs.wsgi

echo "Start $NAME as `whoami`"

cd $DJANGODIR
source ./macs-venv/bin/activate
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHON_PATH=$DJANGODIR:$PYTHON_PATH

RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR

exec ./macs-venv/bin/gunicorn ${DJANGO_WSGI_MODULE}:application \
    --name $NAME \
    --workers $NUM_WORKERS \
    --user=$USER --group=$GROUP \
    --bind=unix:$SOCKFILE \
    --log-level=debug \
    --log-file=- \
    --reload