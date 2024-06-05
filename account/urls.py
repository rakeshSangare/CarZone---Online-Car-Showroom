from django.urls import path  # Import the path function from django.urls
from account import views  # Import the views module from the account app

app_name = 'account'  # Set the application namespace to 'account'

# Define the URL patterns for the account app
urlpatterns = [
    path('login/', views.login, name='login'),  # URL pattern for the login view
    path('register/', views.register, name='register'),  # URL pattern for the register view
    path('logout/', views.logout, name='logout'),  # URL pattern for the logout view
    path('dashboard/', views.dashboard, name='dashboard'),  # URL pattern for the dashboard view
]
