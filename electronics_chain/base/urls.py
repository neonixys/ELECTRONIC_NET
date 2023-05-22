from django.urls import path

from electronics_chain.base.views import *

urlpatterns = [
    path("product/create/", ProductsCreateView.as_view(), name='product-create'),
    path("product/list/", ProductsListView.as_view(), name='products-list'),
    path("product/<int:pk>/update/", ProductUpdateView.as_view(), name='product-update'),
    path("product/<int:pk>/", ProductRetrieveView.as_view(), name='product'),
    path("product/<int:pk>/delete/", ProductDestroyView.as_view(), name='product-delete'),

]
