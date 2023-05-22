from django.db import models
from electronics_chain.base.models import ContactModel, Products


class FactoryStore(ContactModel):
    products = models.ManyToManyField(Products, verbose_name="Продукты")

    class Meta:
        verbose_name = "Завод"
        verbose_name_plural = "Заводы"

    def __str__(self):
        return self.title
