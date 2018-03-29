from django.urls import path
from . import views

#name space url file
app_name = 'articles'

urlpatterns = [
    path('', views.article_list, name='article_list'),
    #name capturing group path/url
    path('<slug:slug>/', views.article_detail, name='article_detail')
]