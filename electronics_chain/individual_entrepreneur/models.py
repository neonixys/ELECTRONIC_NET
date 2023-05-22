from django.db import models
from django.db.models import CASCADE

from electronics_chain.base.models import ContactModel, Products
from electronics_chain.factory.models import FactoryStore


class IndividualEntrepreneur(ContactModel):
    products = models.ManyToManyField(Products, verbose_name="Продукты")
    supplier = models.ForeignKey(FactoryStore, on_delete=CASCADE, verbose_name="Поставщик")
    credit = models.IntegerField(verbose_name="Задолженность")

    objects = models.Manager()

    class Meta:
        ordering = ['created']
        verbose_name = 'Предприниматель'
        verbose_name_plural = 'Предприниматели'

    def __str__(self):
        return self.title
