from django.db import models


class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64, verbose_name='name', blank=True)
    country = models.CharField(max_length=16, verbose_name='country', blank=True)
    email = models.EmailField(max_length=128, verbose_name='email', blank=True)
    phone = models.CharField(max_length=32, verbose_name='phone', blank=True, null=True, unique=True)
    login_bitmain = models.CharField(max_length=128, verbose_name='login_bitmain', unique=True)
    telegram_link = models.CharField(max_length=128, verbose_name='telegram_link', blank=True)
    instagram_link = models.CharField(max_length=128, verbose_name='instagram_link', blank=True)
    twitter_link = models.CharField(max_length=128, verbose_name='twitter_link', blank=True)
    vk_link = models.CharField(max_length=128, verbose_name='vk_link', blank=True)
    facebook_link = models.CharField(max_length=128, verbose_name='facebook_link', blank=True)
    linkedin_link = models.CharField(max_length=128, verbose_name='linkedin_link', blank=True)
    whatsapp_link = models.CharField(max_length=64, verbose_name='whatsapp_link', blank=True)

    class Meta:
        db_table = 'Users'
        verbose_name = 'users'
        verbose_name_plural = 'users'

    def __str__(self):
        return self.name


class Company(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64, verbose_name='Название Компании ')
    url = models.CharField(max_length=128, verbose_name='Ссылка на сайт')
    first_fiz = models.CharField(max_length=64, verbose_name='Физ лицо')
    second_fiz = models.CharField(max_length=64, verbose_name='Второе Физ лицо')
    phone = models.CharField(max_length=64, verbose_name='Номер')
    other_phone = models.CharField(max_length=64, verbose_name='Второй номер')

    class Meta:
        db_table = 'Company'
        verbose_name = 'сompany'
        verbose_name_plural = 'company'



