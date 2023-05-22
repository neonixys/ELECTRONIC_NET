from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe

from electronics_chain.base.admin import clean_credit
from electronics_chain.factory.models import FactoryStore
from electronics_chain.individual_entrepreneur.models import IndividualEntrepreneur


@admin.register(IndividualEntrepreneur)
class IndividualEntrepreneurAdmin(admin.ModelAdmin):
    list_display = ['title', 'email', 'credit', 'supplier']
    list_display_links = ('title',)
    filter_horizontal = ['products']
    actions = (clean_credit,)
    list_filter = ("city",)





