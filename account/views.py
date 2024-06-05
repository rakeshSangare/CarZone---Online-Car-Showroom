from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from contacts.models import Contact
from django.contrib.auth.decorators import login_required

# View for user login
def login(request):
    if request.method == 'POST':  # Check if the request method is POST
        username = request.POST['username']  # Get the username from the POST request
        password = request.POST['password']  # Get the password from the POST request

        user = auth.authenticate(username=username, password=password)  # Authenticate the user

        if user is not None:  # Check if authentication is successful
            auth.login(request, user)  # Log the user in
            messages.success(request, 'You are now logged in')  # Display success message
            return redirect('account:dashboard')  # Redirect to the dashboard
        else:
            messages.error(request, 'Invalid login credentials')  # Display error message
            return redirect('account:login')  # Redirect back to the login page

    return render(request, 'account/login.html')  # Render the login page for GET requests

# View for user registration
def register(request):
    if request.method == 'POST':  # Check if the request method is POST
        firstname = request.POST['firstname']  # Get the first name from the POST request
        lastname = request.POST['lastname']  # Get the last name from the POST request
        username = request.POST['username']  # Get the username from the POST request
        email = request.POST['email']  # Get the email from the POST request
        password = request.POST['password']  # Get the password from the POST request
        confirm_password = request.POST['confirm_password']  # Get the confirm password from the POST request

        if password == confirm_password:  # Check if passwords match
            if User.objects.filter(username=username).exists():  # Check if username already exists
                messages.error(request, 'Username already exists')  # Display error message
                return redirect('account:register')  # Redirect back to the registration page
            elif User.objects.filter(email=email).exists():  # Check if email already exists
                messages.error(request, 'Email already exists')  # Display error message
                return redirect('account:register')  # Redirect back to the registration page
            else:
                # Create a new user
                user = User.objects.create_user(
                    first_name=firstname,
                    last_name=lastname,
                    email=email,
                    username=username,
                    password=password
                )
                auth.login(request, user)  # Log the new user in
                messages.success(request, 'You are now logged in!')  # Display success message
                return redirect('account:dashboard')  # Redirect to the dashboard
        else:
            messages.error(request, 'Passwords do not match')  # Display error message
            return redirect('account:register')  # Redirect back to the registration page

    return render(request, 'account/register.html')  # Render the registration page for GET requests

# View for user logout
def logout(request):
    if request.method == 'POST':  # Check if the request method is POST
        auth.logout(request)  # Log the user out
        messages.success(request, 'You have been logged out successfully!')  # Display success message
        return redirect('pages:home')  # Redirect to the home page
    return redirect('pages:home')  # Redirect to the home page if method is not POST

# Dashboard view, requires login
@login_required(login_url='account:login')  # Ensure the user is logged in to access this view
def dashboard(request):
    # Get the user's inquiries ordered by creation date
    user_inquiries = Contact.objects.order_by('-created_date').filter(user_id=request.user.id)
    context = {
        'inquiries': user_inquiries,  # Add inquiries to the context
    }
    return render(request, 'account/dashboard.html', context)  # Render the dashboard page with user inquiries
