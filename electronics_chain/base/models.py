from django.contrib.contenttypes.models import ContentType
from django.db import models


class ContactModel(models.Model):
    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"

    title = models.CharField(max_length=150, verbose_name="Название")
    email = models.EmailField()
    country = models.CharField(max_length=200, verbose_name="Страна", blank=True, null=True)
    city = models.CharField(max_length=100, verbose_name="Город", blank=True, null=True)
    street = models.CharField(max_length=80, verbose_name="Улица", blank=True, null=True)
    building_num = models.IntegerField(verbose_name="Номер дома", blank=True, null=True)
    created = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True)


class Products(models.Model):
    title = models.CharField(max_length=150, verbose_name="Название")
    product_model = models.CharField(max_length=100, verbose_name="Модель")
    release_date = models.DateField(null=True, blank=True, verbose_name='Дата выхода продукта на рынок')

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    def __str__(self):
        return self.title
