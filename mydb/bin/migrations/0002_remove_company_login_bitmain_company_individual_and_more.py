# Generated by Django 4.2.3 on 2023-07-28 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bin', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='login_bitmain',
        ),
        migrations.AddField(
            model_name='company',
            name='individual',
            field=models.CharField(blank=True, max_length=64, verbose_name='Первое Физ-Лицо'),
        ),
        migrations.AddField(
            model_name='company',
            name='individual2',
            field=models.CharField(blank=True, max_length=64, verbose_name='Второе Физ-Лицо'),
        ),
    ]
