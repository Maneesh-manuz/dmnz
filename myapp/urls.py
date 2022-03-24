from django.urls import re_path
from .import views

urlpatterns = [
    re_path(r'^$', views.admin_payment_history, name='admin_payment_history'),
    re_path(r'^payment_table$', views.payment_table, name='payment_table'),

]
