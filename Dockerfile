FROM python:3.6.1-alpile

WORKDIR /code

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD gunicorn -w 4 -b 0.0.0.0:8000 --log-level DEBUG run:app
