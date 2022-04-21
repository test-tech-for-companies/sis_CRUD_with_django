from django.urls import path
from applications.authen import views

urlpatterns = [
    path('login/',views.LoginView.as_view(), name='login'),
    path('signup/',views.SignUpView.as_view(), name='signup')
]