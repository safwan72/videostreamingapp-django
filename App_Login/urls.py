
from django.urls import path
from App_Login.views import signupview,loginview,logoutview,profileupdate

app_name='App_Login'

urlpatterns = [
    path('', signupview,name='signup'),
    path('login/', loginview,name='login'),
    path('logout/', logoutview,name='logout'),
    path('profile/', profileupdate,name='profile'),
]

