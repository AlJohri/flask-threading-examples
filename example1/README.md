# example1

This is an example spawning a background thread using [`threading`](https://docs.python.org/3/library/threading.html) from the python standard library with [Flask](http://flask.pocoo.org/) and [gunicorn](http://gunicorn.org/). You can also try it with Flask's default web server, [Werkzeug](http://werkzeug.pocoo.org/).

## Docker

```
docker-compose up --build
```

## Local

```
pipenv install
./start.sh
```

#### Links

Gunicorn
- http://docs.gunicorn.org/en/stable/design.html
- https://github.com/benoitc/gunicorn/issues/1045

Werzkeug
- http://werkzeug.pocoo.org/docs/0.13/serving/
