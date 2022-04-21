from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('applications.users.urls'), name='users'),
    path('', include('applications.authen.urls'), name='authen')
]
