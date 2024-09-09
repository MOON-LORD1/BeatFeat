from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("accounts/login/",views.login_user , name="login"),
    path("accounts/registration/",views.register_user , name="registration"),
    path("accounts/logout/",views.logout_user , name="logout"),
]