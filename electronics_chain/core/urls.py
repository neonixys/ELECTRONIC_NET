from django.urls import path

from electronics_chain.core import views

urlpatterns = [
    path('signup', views.UserCreateView.as_view(), name='signup'),
]