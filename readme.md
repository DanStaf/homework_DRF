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
- 