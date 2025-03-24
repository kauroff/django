from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='наименование')
    description = models.TextField(**NULLABLE, verbose_name='описание')

    # created_at = models.DateTimeField(**NULLABLE, verbose_name='создание')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name='наименование')
    description = models.TextField(**NULLABLE, verbose_name='описание')
    image = models.ImageField(upload_to='products/', **NULLABLE, verbose_name='изображение')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='категория')
    unit_price = models.IntegerField(verbose_name='цена за штуку')
    create_date = models.DateTimeField(verbose_name='дата создания', auto_now_add=True)
    edit_date = models.DateTimeField(verbose_name='дата изменения', auto_now=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'


class Contact(models.Model):
    city = models.CharField(max_length=50, verbose_name='город')
    address = models.CharField(max_length=50, verbose_name='адрес')
    phone = models.CharField(max_length=12, verbose_name='номер')

    def __str__(self):
        return f'{self.city} {self.phone}'

    class Meta:
        verbose_name = 'контакт'
        verbose_name_plural = 'контакты'
