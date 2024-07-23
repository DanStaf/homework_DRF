from django.db import models
from users.models import User


class Course(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    picture = models.ImageField(null=True, blank=True, verbose_name='Превью (картинка)')
    owner = models.ForeignKey(User, null=True, blank=True, verbose_name='Владелец', on_delete=models.SET_NULL)

    def __str__(self):
        return f'Course: {self.title}'

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'


class Lesson(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    picture = models.ImageField(null=True, blank=True, verbose_name='Превью (картинка)')
    url = models.CharField(max_length=150, null=True, blank=True, verbose_name='Ссылка на видео')
    course = models.ForeignKey(Course, null=True, blank=True, verbose_name='Курс', on_delete=models.SET_NULL)
    owner = models.ForeignKey(User, null=True, blank=True, verbose_name='Владелец', on_delete=models.SET_NULL)

    def __str__(self):
        return f'Lesson: {self.title}'

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'
