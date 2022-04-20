from django.contrib import admin
from django.urls import path
from applications.users  import views
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', views.UserCreateView.as_view()),

]
