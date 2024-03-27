FROM node:alpine as frontend
WORKDIR /app
COPY index.html script.js /app/

FROM python:3.9-slim as backend
WORKDIR /app
COPY app.py requirements.txt /app/
RUN pip install -r requirements.txt

FROM mongo:latest as database

FROM backend as builder
RUN echo "Building..."

FROM builder
COPY --from=frontend /app /app

CMD ["python", "app.py"]
