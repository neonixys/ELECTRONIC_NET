from django.contrib import admin

from electronics_chain.factory.models import FactoryStore


@admin.register(FactoryStore)
class FactoryStoreAdmin(admin.ModelAdmin):
    ordering = ("title",)
    list_filter = ("city",)
