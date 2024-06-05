from django.shortcuts import render, redirect  # Import render and redirect functions from Django's shortcuts module
from contacts.models import Contact  # Import the Contact model from the contacts app
from django.contrib import messages  # Import the messages module for displaying messages
from django.contrib.auth.models import User  # Import the User model from Django's authentication module
from django.core.mail import send_mail  # Import the send_mail function from Django's mail module
from django.views.decorators.csrf import csrf_protect  # Import csrf_protect decorator

# Create your views here.

@csrf_protect
def inquiry(request):
    # Check if the request method is POST
    if request.method == 'POST':
        # Extract data from the POST request
        user_id = request.POST['user_id']
        car_id = request.POST['car_id']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        customer_need = request.POST['customer_need']
        car_title = request.POST['car_title']
        city = request.POST['city']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']

        # Check if the user is authenticated
        if request.user.is_authenticated:
            user_id = request.user.id
            # Check if the user has already made an inquiry about this car
            has_contacted = Contact.objects.all().filter(car_id=car_id, user_id=user_id)
            if has_contacted:
                messages.error(request, "You have already made an inquiry about this car. Please wait until we get back to you!!")
                return redirect('/cars/' + car_id)

        # Create a new Contact instance with the extracted data
        contact = Contact(user_id=user_id, car_id=car_id, first_name=first_name, last_name=last_name,
                          customer_need=customer_need, car_title=car_title, city=city, email=email,
                          phone=phone, message=message)

        # Get admin email address
        admin_info = User.objects.get(is_superuser=True)
        admin_email = admin_info.email

        # Send email notification to admin about the new car inquiry
        send_mail(
            "New Car Inquiry",
            "You have new car inquiry " + car_title + ". Please login to admin panel for more info.",
            "admin@gmail.com",
            [admin_email],
            fail_silently=False,
        )

        # Save the contact instance to the database
        contact.save()

        # Display success message
        messages.success(request, "Your request has been submitted. We will get back to you shortly!!")

        # Redirect to the car detail page
        return redirect('/cars/' + car_id)
