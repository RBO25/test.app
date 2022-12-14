# Generated by Django 4.1.2 on 2022-11-01 11:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.IntegerField(unique=True, verbose_name='Номер телефона')),
                ('login', models.CharField(max_length=15, unique=True, verbose_name='Логин')),
                ('password', models.CharField(max_length=15, verbose_name='Пароль')),
                ('birth', models.DateField(verbose_name='Дата рождения')),
                ('tg', models.CharField(max_length=15, unique=True, verbose_name='Telegram (не обязательно)')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email (не обязательно)')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Имя')),
            ],
        ),
    ]
