from django.urls import path
from applications.users import views

urlpatterns = [
    path('user/',views.UserCreateView.as_view(), name='create_user'),
    path('detail/<int:pk>/', views.UserDetailView.as_view(), name='detail-user'),
    path('change/<int:pk>/', views.UserUpdateView.as_view(), name='update-user'),
    path('no-user/<int:pk>/', views.UserDeleteView.as_view(), name='delete-user'),     
]