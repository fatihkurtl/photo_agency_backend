FROM python:3.11-slim AS django

WORKDIR /photo_agency_backend

COPY ./requirements.txt /photo_agency_backend/

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN python3 manage.py collectstatic --noinput

FROM nginx:alpine

COPY --from=django /photo_agency_backend/staticfiles /usr/share/nginx/html/static
COPY --from=django /photo_agency_backend/media /usr/share/nginx/html/media

COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

CMD ["gunicorn", "--bind", "0.0.0.0:8080", "core.wsgi:application"]
