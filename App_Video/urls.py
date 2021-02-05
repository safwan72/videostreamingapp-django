
from django.urls import path
from .views import Home,detail_view
app_name='App_Video'
urlpatterns = [
    path('',Home.as_view(),name='home'),
    path('details/<pk>/',detail_view,name='details'),
]