# modern-django-sandbox

[djstein/modern-django](https://github.com/djstein/modern-django)

## Setup

```sh
# Copy secret file
cp env.sample .env

# Activate venv
source venv/bin/activate

# Install packages
pip install -Ur requirements/local.txt

# Migrate
python manage.py migrate

# Run server
./manage.py runserver

# Create user
curl -X POST -H 'Accept: application/json' --data 'username=hoge&email=hoge@example.com' http://localhost:8000/users/

# Show users list
curl -X GET -H 'Accept: application/json' http://localhost:8000/users/
```

## License

MIT
