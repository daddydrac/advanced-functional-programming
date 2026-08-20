.PHONY: init up down destroy logs test check chapter-test

init:
	docker compose --profile tools run --rm --user "$$(id -u):$$(id -g)" init

up:
	docker compose up --build -d

down:
	docker compose down

destroy:
	docker compose down --volumes --remove-orphans

logs:
	docker compose logs -f api

test:
	docker compose --profile tools run --rm --build test

chapter-test:
	test -n "$(CHAPTER)"
	docker compose --profile tools run --rm --build -e CHAPTER="$(CHAPTER)" test

check:
	docker compose --profile tools run --rm --build test
