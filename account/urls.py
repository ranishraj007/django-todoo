from django.urls import include, path

from account.views import login

urlpatterns = [
    path('login/', login, name='login'),
]
