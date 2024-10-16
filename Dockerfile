FROM python:3.11-slim
WORKDIR /my_blog
COPY ./requirements.txt /my_blog
RUN pip install -r requirements.txt
COPY . .
RUN python3 manage.py collectstatic --noinput

EXPOSE 80
CMD ["gunicorn", "--bind", "0.0.0.0:80", "core.wsgi:application"]