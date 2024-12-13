# homework / DRF

## 24.1

### Used technologies:
- Python
- Postgres
- Django
- DRF
- django_filters 
- JWT

### Models
- app users, models User, Payment
- app online_learning, models Course, Lesson

### Views:
- for Course and User used ViewSets
- for Lesson used Generics

## 24.2

Custom serializers added for:
- Course (lessons and lessons_qty)
- Payment (filters)
- User (payments)

## 25.1

added Moderators and Owners permissions via JWT

## 25.2

- validator added for Lesson.url
- Subscription added
- pagination for Lesson and Course added
- tests added

## 26.1

- added drf_yasg
- added stripe, added endpoint for payment creation
- added PaymentRetrieve endpoint

## 26.2
- added celery, eventlet, redis, django-celery-beat (+migrate)
- async send emails (updates on course)
- # redis-cli / ... / shutdown / ... / exit
- # redis-server
- # python manage.py runserver
- # celery -A config worker -l INFO -P eventlet
- deactivate sleeping users
- # redis-server
- # python manage.py runserver
- # celery -A config worker -l INFO -P eventlet
- # celery -A config beat --loglevel INFO


## 27.2 Docker
1) install and start Docker Desktop
2) ??????? ?? ?????? Sign out ? Docker Desktop
3) ? ?????????? ?????????????? ?????? Docker Engine
4) ???????? ????? ? ??????? ???????: `docker-compose build`
5) ????????? ?????????? ? ??????? ???????: `docker-compose up` ??? `docker-compose up -d --build`
