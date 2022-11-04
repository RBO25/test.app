from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Client(models.Model):
    phone = models.IntegerField(verbose_name="Номер телефона", unique=True)
    login = models.CharField(verbose_name="Логин", max_length=15, unique=True)
    password = models.CharField(verbose_name="Пароль", max_length=15)
    # name = models.CharField(verbose_name='Имя', max_length=50)
    birth = models.DateField(verbose_name="Дата рождения", null=True)
    tg = models.CharField(verbose_name="Telegram (не обязательно)", max_length=15, blank=True, null=True)
    email = models.EmailField(verbose_name="Email (не обязательно)", blank=True, null=True)
    name = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE)