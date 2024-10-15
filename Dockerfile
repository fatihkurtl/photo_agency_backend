FROM python:3.11-slim
WORKDIR /photo_agency_backend
COPY ./requirements.txt /photo_agency_backend/
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
RUN python3 manage.py collectstatic --noinput

FROM nginx:alpine
COPY --from=0 /photo_agency_backend/staticfiles /usr/local/django_app/static
COPY --from=0 /photo_agency_backend/media /usr/local/django_app/media
COPY nginx.conf /etc/nginx/conf.d/default.conf

COPY --from=0 /photo_agency_backend /photo_agency_backend
WORKDIR /photo_agency_backend

CMD nginx && gunicorn your_project.wsgi:application --bind 0.0.0.0:8000