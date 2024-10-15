FROM python:3-alpine AS builder
 
WORKDIR /photo_agency_backend
 
RUN python3 -m venv venv
ENV VIRTUAL_ENV=/photo_agency_backend/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
 
COPY requirements.txt .
RUN pip install -r requirements.txt
 
# Stage 2
FROM python:3-alpine AS runner
 
WORKDIR /photo_agency_backend
 
COPY --from=builder /photo_agency_backend/venv venv
COPY example_django example_django
 
ENV VIRTUAL_ENV=/photo_agency_backend/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
ENV PORT=8000
 
EXPOSE ${PORT}
 
CMD gunicorn --bind :${PORT} --workers 2 example_django.wsgi