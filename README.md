# ravenpack-back


###To run:
Install redis, or modify in pizzaloversproject/settings to use an in-memory channel instead of redis

(Redis installation: https://www.digitalocean.com/community/tutorials/how-to-install-and-configure-redis-on-ubuntu-16-04)

(before, add JWT token in pizzaloversproject/settings.py)

pip install -r requirements.txt

cd pizzaloversproject

python manage.py makemigrations

python manage.py migrate

python manage.py runserver



