db: down
	docker compose up -d db
	sleep 10
	. ../../venv/bin/activate; python init-db.py


down:
	docker compose down

workers:
	docker compose up -d --build django-workers 

server:
	docker compose up -d  --build django 