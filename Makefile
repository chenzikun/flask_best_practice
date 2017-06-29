.CHENZIKUN: make
help:
	@echo "make gulp | up | reset | stop_all | rm_all"

gulp:
	@cd static/application;nohup gulp server &

gup:
	@nohup gunicorn -w 4 -b 127.0.0.1:8080 run:app &

reset:
	@git fetch; git reset --hard origin/master;git pull

stop_all:
	@docker stop `docker ps -q`

rm_all:
	@docker rm `docker ps -aq`

dup:
	@docker run -d -p 8800:8000 demo:v0.2.1
