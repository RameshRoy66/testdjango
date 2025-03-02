from django.urls import path
from .views import register, success,get_logins, get_login_by_id, create_login, update_login, delete_login


urlpatterns = [
    path('register/', register, name='register'),
    path('success/', success, name='success'),
    path('api/logins/', get_logins, name='get_logins'),  # Get all users
    path('api/logins/<int:id>/', get_login_by_id, name='get_login_by_id'),  # Get by ID
    path('api/logins/create/', create_login, name='create_login'),  # Create user
    path('api/logins/update/<int:id>/', update_login, name='update_login'),  # Update user
    path('api/logins/delete/<int:id>/', delete_login, name='delete_login'),  # Delete user

]
