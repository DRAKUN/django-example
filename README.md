# django-example

```sh

pip install pillow
pip install psycopg2
pip install psycopg2-binary

./manage.py makemigrations
./manage.py makemigrations
./manage.py sqlmigrate listings 0001
./manage.py migrate
./manage.py createsuperuser
```

## Adding gitpod file to your dev branch

ports:
- port: 8080
  onOpen: open-preview
  tasks:
  - init: >
      python3 -m pip install -r requirements.txt && 
      python3 manage.py migrate
    command: >
      echo "from locallibrary.settings import *" > locallibrary/local_settings.py &&
      echo "ALLOWED_HOSTS = ['*']" >> locallibrary/local_settings.py &&
      export DJANGO_SETTINGS_MODULE=locallibrary.local_settings &&
      python3 manage.py runserver 0.0.0.0:8080
  github:
    prebuilds:
      pullRequestsFromForks: true

