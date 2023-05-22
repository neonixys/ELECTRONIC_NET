from django.urls import path

from electronics_chain.individual_entrepreneur.views import *

urlpatterns = [
    path("entrepreneur/create/", EntrepreneurCreateView.as_view(), name='entrepreneur-create'),
    path("entrepreneur/<int:pk>/update/", EntrepreneurUpdateView.as_view(), name='entrepreneur-update'),
    path("entrepreneur/list/", EntrepreneurListView.as_view(), name='entrepreneur-list'),
    path("entrepreneur/<int:pk>/", EntrepreneurRetrieveView.as_view(), name='entrepreneur'),
    path("entrepreneur/<int:pk>/delete/", EntrepreneurDestroyView.as_view(), name='entrepreneur-delete'),
]