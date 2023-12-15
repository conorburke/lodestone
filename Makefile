up:
	docker compose up -d

uplogs:
	docker compose up

stop:
	docker compose stop

down:
	docker compose down

.phony: up uplogs stop down
