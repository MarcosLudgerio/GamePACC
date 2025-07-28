from django.urls import path
from .views import ViewCreate, LoginPersonal, redirect_view

app_name = 'users'

urlpatterns = [
    path('create/', ViewCreate.as_view(), name='create'),
    path('login/', LoginPersonal.as_view(), name='login'),
    path('', LoginPersonal.as_view(), name='login'),
    path('redirect/', redirect_view, name='redirect'),
]