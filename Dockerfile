FROM python:3.11-slim

WORKDIR /photo_agency_backend

COPY ./requirements.txt /photo_agency_backend/

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN python3 manage.py collectstatic --noinput

RUN mkdir -p media && chmod -R 755 media

EXPOSE 80

CMD ["gunicorn", "--bind", "0.0.0.0:80", "core.wsgi:application"]
