from django.urls import re_path
from .import views

urlpatterns = [
    re_path(r'^admin_payment_history$', views.admin_payment_history, name='admin_payment_history'),
    re_path(r'^$', views.demo, name='demo'),
    
    
]
