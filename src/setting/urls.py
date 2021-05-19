from django.urls import path
from . import views



app_name='setting'


urlpatterns = [
    path('',views.Home,name='Home'),
    path('<str:name_category>/', views.filter_by_category,name='filter_by_category'),

    ]