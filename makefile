docker-up:
	docker compose up --build -d
	docker exec -it python-movie-scheduler-app python consola_peliculas.py

docker-down:
	docker compose down