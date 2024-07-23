from django.db import models
from django.contrib.auth.models import AbstractUser

# from online_learning.models import Course, Lesson


class User(AbstractUser):
    username = None

    email = models.EmailField(verbose_name='Почта', unique=True)
    avatar = models.ImageField(null=True, blank=True, verbose_name='Аватар')
    phone = models.CharField(null=True, blank=True, max_length=150, verbose_name='Телефон')
    country = models.CharField(null=True, blank=True, max_length=150, verbose_name='Страна')

    token = models.CharField(null=True, blank=True, max_length=150, verbose_name='Token')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):

        if self.first_name and self.last_name:
            return f'USER: {self.first_name} {self.last_name}'
        else:
            return f'USER: {self.email}'


class Payment(models.Model):

    CASH = "наличные"
    CARD = "перевод на счет"

    PAYMENT_CHOICES = [
        (CASH, "наличные"),
        (CARD, "перевод на счет")
    ]

    owner = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    payment_date = models.DateField(verbose_name='Дата оплаты')
    course = models.ForeignKey("online_learning.Course", null=True, blank=True, verbose_name='Оплаченный курс', on_delete=models.CASCADE)
    lesson = models.ForeignKey("online_learning.Lesson", null=True, blank=True, verbose_name='Оплаченный урок', on_delete=models.CASCADE)
    value = models.PositiveIntegerField(verbose_name='Сумма оплаты')
    payment_method = models.CharField(max_length=150, choices=PAYMENT_CHOICES, verbose_name='Способ оплаты')

    class Meta:
        verbose_name = 'платёж'
        verbose_name_plural = 'платежи'

    def __str__(self):
        return f'Payment: {self.payment_date} / {self.value}'
