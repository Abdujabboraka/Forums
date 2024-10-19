from django.urls import path
from .views import homepage, mavzu_detail, add_mavzu, register_view, login_view, logout_view

urlpatterns = [
    path('', homepage, name='homepage'),
    path('detail/<int:pk>/', mavzu_detail, name='detail'),
    path('add/', add_mavzu, name='add_mavzu'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]