from django.urls import path  # Import the path function from Django's URL module
from cars import views  # Import the views module from the cars app

app_name = 'cars'  # Define the namespace for the cars app

# Define URL patterns for the cars app
urlpatterns = [
    path('', views.cars, name='cars'),  # URL pattern for displaying all cars, mapped to the cars view function
    path('<int:id>', views.car_detail, name='car_detail'),  # URL pattern for displaying details of a specific car, mapped to the car_detail view function
    path('search/', views.search, name='search'),  # URL pattern for handling car search functionality, mapped to the search view function
]
