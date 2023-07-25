from django.db import models


class User(models.Model):
    name = models.CharField(
        max_length=64,
        verbose_name='name',
        blank=True
    )
    username = models.CharField(
        max_length=128,
        verbose_name='username',
        blank=True
    )
    email = models.EmailField(
        max_length=128,
        verbose_name='email',
        blank=True
    )
    phone = models.CharField(
        max_length=32,
        verbose_name='phone',
        blank=True,
        null=True
    )
    messanger = models.ForeignKey(
        'Messanger',
        on_delete=models.CASCADE,
        verbose_name='мессенджеры',
        null=False,
        blank=False
    )

    class Meta:
        db_table = 'Users'
        verbose_name = 'users'
        verbose_name_plural = 'users'

    def __str__(self):
        return self.name





class Messanger(models.Model):
    name = models.CharField(
        max_length=32,
        verbose_name='category-messanger'
    )
    is_published = models.BooleanField(
        default=True,
        verbose_name='published'
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Messanger'
        verbose_name = 'messanger'
        verbose_name_plural = 'messangers'

