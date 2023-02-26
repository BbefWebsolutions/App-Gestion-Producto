from django.urls import path

from appInicio import views
# from appInicio import dx

urlpatterns = [
    path('', views.inicio, name='inicio'),
]