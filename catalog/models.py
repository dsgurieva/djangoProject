from django.db import models

from user.models import User


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='наименование')
    description = models.TextField(verbose_name='описание')
    preview = models.ImageField(upload_to='products/', verbose_name='превью', null=True, blank=True)
    category = models.CharField(max_length=150, verbose_name='категория')
    price = models.IntegerField(verbose_name='цена')
    date_of_creation = models.DateField(verbose_name='дата создания')
    last_modified_date = models.DateField(verbose_name='дата последнего изменения')
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return f'{self.name} {self.price} руб./кг.'


    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ('name',)



class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='наименование')
    description = models.TextField(verbose_name='описание')


    def __str__(self):
        return f'{self.id} {self.name}'


    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ('name',)


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='продукт', related_name='product_ver')
    number_version = models.IntegerField(default=0, verbose_name='номер версии')
    name_version = models.CharField(max_length=100, verbose_name='название версии')
    is_active = models.BooleanField(default=False, verbose_name='признак текущей версии')


    def __str__(self):
        return f'{ self.number_version} {self.name_version}'


    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'