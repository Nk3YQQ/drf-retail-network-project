run:
	docker-compose up --build -d

stop:
	docker-compose down

run-for-test:
	docker-compose -f docker-compose.dev.yml up --build -d

tests:
	docker-compose -f docker-compose.dev.yml exec -T app python3 manage.py test

clean:
	docker-compose -f docker-compose.dev.yml down --volumes
