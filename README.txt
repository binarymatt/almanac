almanac README
==================

Getting Up and Running
---------------

- cd <directory containing this file>

- $venv/bin/python setup.py develop

- $venv/bin/alembic upgrade head

- $venv/bin/pserve development.ini

Notes:
------
As of right now I've got the sqlalchemy url hardcoded. If you want to run off of your own 
postgres db, make sure to set the dsn in the ALMANAC_DATABASE_URL env variable
