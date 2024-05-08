from django.urls import path
# from .views import login_view
# from .forms import SignupForm
from . import views

urlpatterns = [
    path('login/',views.loginPage,name="login"),
   path('register',views.register,name="register"),
    path('',views.customer, name='customer'),
    path('logout',views.LogoutPage,name="logout"),
    path('home', views.home_view, name='home'),
    path('user_deposit', views.user_deposit, name='user_deposit'),
    path('user_withdrawl', views.user_withdrawl, name='user_withdrawl'),
    path('user_balance', views.user_balance, name='user_balance'),
   
]