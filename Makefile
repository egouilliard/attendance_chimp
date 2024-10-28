.PHONY: build start stop

build:
	docker-compose build

start:
	docker-compose up

stop:
	docker-compose down
