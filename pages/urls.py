from django.urls import path  # Import path function from Django's URL patterns module
from pages import views  # Import views module from the pages app

app_name = 'pages'  # Define the app namespace

urlpatterns = [
    # Define URL pattern for the home page, mapping it to the home view function
    path('', views.home, name="home"),

    # Define URL pattern for the about page, mapping it to the about view function
    path('about/', views.about, name="about"),

    # Define URL pattern for the services page, mapping it to the services view function
    path('services/', views.services, name='services'),

    # Define URL pattern for the contact page, mapping it to the contact view function
    path('contact/', views.contact, name='contact'),
]
