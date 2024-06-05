from django.shortcuts import render  # Import render function from Django's shortcuts module
from pages.models import Team  # Import the Team model from the pages app
from cars.models import Car  # Import the Car model from the cars app
from django.contrib.auth.models import User  # Import the User model from Django's authentication module
from django.core.mail import send_mail  # Import the send_mail function from Django's mail module

# Create your views here.

def home(request):
    # Retrieve distinct values for model, city, year, and body style from the Car model
    model_search = Car.objects.values_list('model', flat=True).distinct()
    city_search = Car.objects.values_list('city', flat=True).distinct()
    year_search = Car.objects.values_list('year', flat=True).distinct()
    body_style_search = Car.objects.values_list('body_style', flat=True).distinct()

    # Retrieve featured cars ordered by creation date
    featured_cars = Car.objects.order_by('-created_date').filter(is_featured=True)

    # Retrieve all cars ordered by creation date
    all_cars = Car.objects.order_by('-created_date')
    
    # Retrieve all teams
    teams = Team.objects.all()

    # Prepare data to be passed to the template
    data = {
        'model_search': model_search,
        'city_search': city_search,
        'year_search': year_search,
        'body_style_search': body_style_search,
        'featured_cars': featured_cars,
        'all_cars': all_cars,
        'teams': teams,
    }

    # Render the home template with the provided data
    return render(request, 'pages/home.html', data)

def about(request):
    # Retrieve all teams
    teams = Team.objects.all()

    # Prepare data to be passed to the template
    data = {
        'teams': teams
    }

    # Render the about template with the provided data
    return render(request, 'pages/about.html', data)

def services(request):
    # Render the services template
    return render(request, 'pages/services.html')

def contact(request):
    # Handle POST request for contacting
    if request.method == 'POST':
        # Extract form data
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        phone = request.POST['phone']
        message = request.POST['message']

        # Get admin email address
        admin_info = User.objects.get(is_superuser=True)
        admin_email = admin_info.email

        # Prepare email subject and body
        email_subject = 'You have a new message from Carzone website regarding ' + subject
        email_body = 'Name: ' + name + ', Email: ' + email + ', Phone: ' + phone + ', Message: ' + message

        # Send email to admin
        send_mail(
            email_subject,
            email_body,
            "admin@gmail.com",
            [admin_email],
            fail_silently=False,
        )

    # Render the contact template
    return render(request, 'pages/contact.html')
