FROM python:3.11-slim AS django

WORKDIR /usr/local/django_app

COPY ./requirements.txt /usr/local/django_app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN python3 manage.py collectstatic --noinput

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "core.wsgi:application"]
