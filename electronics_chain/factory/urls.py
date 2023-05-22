from django.urls import path

from electronics_chain.factory.views import *

urlpatterns = [
    path("factory/create/", FactoryStoreCreateView.as_view(), name='factory-create'),
    path("factory/<int:pk>/update/", FactoryStoreUpdateView.as_view(), name='factory-update'),
    path("factory/list/", FactoryStoreListView.as_view(), name='factory-list'),
    path("factory/<int:pk>/", FactoryStoreRetrieveView.as_view(), name='factory'),
    path("factory/<int:pk>/delete/", FactoryStoreDestroyView.as_view(), name='factory-delete'),
]