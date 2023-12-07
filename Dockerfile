FROM python:3.11.7-alpine
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
WORKDIR /app/flaskapp
CMD ["flask","run","--host","0.0.0.0"]