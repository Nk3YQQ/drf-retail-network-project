run:
	docker-compose up --build -d

entrypoint:
	python3 manage.py migrate
	python3 manage.py collectstatic --noinput
	gunicorn --config gunicorn_config.py config.wsgi:application

stop:
	docker-compose down

build-for-test:
	docker-compose -f docker-compose.dev.yml up --build -d
	docker-compose -f docker-compose.dev.yml exec -T app python3 config/settings.py

status:
	docker-compose -f docker-compose.dev.yml ps

logs:
	docker-compose -f docker-compose.dev.yml logs

tests:
	docker-compose -f docker-compose.dev.yml exec -T app python3 manage.py test

clean:
	docker-compose -f docker-compose.dev.yml down --volumes
