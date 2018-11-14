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
```

## License

MIT
