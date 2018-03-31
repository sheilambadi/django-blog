from django.urls import path
from . import views

#name space url file
app_name = 'accounts'

urlpatterns = [
    path('', views.signup_view, name='signup') 
]