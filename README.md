# README #

This README would normally document whatever steps are necessary to get your application up and running.
This is a Django Boilerplate Quickstart Kit to boot up any Django microservice quickly.

### Dependencies ###

* Python 3.x
* MySQL 5.x


### Virtual Environment Setup ###

* Setup bagon virtualenv : "virtualenv -p python3.6 bagon"
* Move to virtualenv and activate its environment


### Dependency Setup ###

* Install requirements: "pip install -r requirements.txt".
* Change webapp/conf/env/conf.py as per your setup
* Run migrations: "python manage.py migrate"
* Create superuser: "python manage.py createsuperuser"
* Start Server: "python manage.py runserver"


### Celery App Setup (If Needed) ###
..bin/celery -A webapp.celery_app worker -Q my --loglevel=WARNING


### API Documentation ###

- Create Ticket

```
curl --location --request POST 'http://localhost:8888/api/v1/tickets' \
--header 'Content-Type: application/json' \
--data-raw '{
	"facility_id": 2,
	"vehicle_type": "BIKE",
	"reg_no": "KA 01 BB 1234"
}'
```

- Close Ticket

```
curl --location --request PUT 'http://localhost:8888/api/v1/tickets' \
--header 'Content-Type: application/json' \
--data-raw '{
	"ticket_id": 10
}'
```


- Get Vehicle Tickets

```
curl --location --request GET 'http://localhost:8888/api/v1/tickets?reg_no=KA%2001%20HH%201234' \
--data-raw ''

```