FROM python:3.11-slim
WORKDIR /photo_agency_backend
COPY ./requirements.txt /photo_agency_backend
RUN pip install -r requirements.txt
COPY . .
RUN python3 manage.py collectstatic --noinput

EXPOSE 80
CMD ["gunicorn", "--bind", "0.0.0.0:80", "core.wsgi:application"]