# Generated by Django 4.1.2 on 2022-11-02 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0002_alter_client_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email (не обязательно)'),
        ),
        migrations.AlterField(
            model_name='client',
            name='tg',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='Telegram (не обязательно)'),
        ),
    ]