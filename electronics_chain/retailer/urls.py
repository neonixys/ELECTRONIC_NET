from django.urls import path

from electronics_chain.retailer.views import RetailerCreateView, RetailerUpdateView, RetailerListView, \
    RetailerRetrieveView, RetailerDestroyView

urlpatterns = [
    path("retailer/create/", RetailerCreateView.as_view(), name='retailer-create'),
    path("retailer/<int:pk>/update/", RetailerUpdateView.as_view(), name='retailer-update'),
    path("retailer/list/", RetailerListView.as_view(), name='retailer-list'),
    path("retailer/<int:pk>/", RetailerRetrieveView.as_view(), name='retailer'),
    path("retailer/<int:pk>/delete/", RetailerDestroyView.as_view(), name='retailer-delete'),
]
