FROM python:3.11-slim AS django

WORKDIR /photo_agency_backend

COPY ./requirements.txt /photo_agency_backend/
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN python3 manage.py collectstatic --noinput

FROM nginx:alpine

COPY --from=django /photo_agency_backend/staticfiles /usr/local/django_app/static
COPY --from=django /photo_agency_backend/media /usr/local/django_app/media 

COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
