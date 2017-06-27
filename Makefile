.CHENZIKUN: make
help:
	@echo "make gulp"

gulp:
	@cd static/application;nohup gulp server &

up:
	@gunicorn -w 4 -b 127.0.0.1:8080 run:app
