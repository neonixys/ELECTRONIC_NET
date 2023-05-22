from django.utils.safestring import mark_safe
from django.utils.translation import ngettext
from django.contrib import admin, messages
from electronics_chain.base.models import ContactModel, Products


@admin.register(ContactModel)
class ContactModel(admin.ModelAdmin):
    list_display = ['title', 'country', 'city', 'street', 'building_num']
    list_filter = ("country",)


@admin.register(Products)
class Products(admin.ModelAdmin):
    list_display = ['title', 'product_model', 'release_date']
    ordering = ['-release_date', 'title']


@admin.action(description="Очистить задолженность")
def clean_credit(modeladmin, request, queryset):
    updated = queryset.update(credit=0)
    modeladmin.message_user(
        request,
        ngettext(
            "%d задолженность была обнулена.",
            "%d задолженности были обнулены.",
            updated,
        )
        % updated,
        messages.SUCCESS,
    )