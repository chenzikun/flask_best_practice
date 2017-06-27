.CHENZIKUN: make
help:
	@echo "make gulp | up | reset"

gulp:
	@cd static/application;nohup gulp server &

up:
	@nohup gunicorn -w 4 -b 127.0.0.1:8080 run:app &

reset:
	@git fetch; git reset --hard origin/master;git pull
