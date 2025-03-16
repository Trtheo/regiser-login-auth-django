from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


# Define a view function for the home page
def home(request):
    return render(request, 'authentication/home.html')


# Define a view function for the login page
def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Check if a user with the provided username exists
        if not User.objects.filter(username=username).exists():
            messages.error(request, 'Invalid Username')
            return redirect('/login/')

        # Authenticate the user with the provided username and password
        user = authenticate(username=username, password=password)
        if user is None:
            messages.error(request, "Invalid Password")
            return redirect('/login/')
        else:
            # Log in the user and redirect to the dashboard after successful login
            login(request, user)
            return redirect('/dashboard/')

    # Render the login page template (GET request)
    return render(request, 'authentication/login.html')


# Define a view function for the registration page
def register_page(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Check if a user with the provided username already exists
        user = User.objects.filter(username=username)
        if user.exists():
            messages.info(request, "Username already taken!")
            return redirect('/register/')

        # Create a new User object with the provided information
        user = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username
        )
        # Set the user's password and save the user object
        user.set_password(password)
        user.save()

        messages.info(request, "Account created Successfully!")
        return redirect('/login/')  # Redirect to login after registration

    # Render the registration page template (GET request)
    return render(request, 'authentication/register.html')


# Define a view function for the dashboard page (login required)
@login_required
def dashboard(request):
    return render(request, 'authentication/dashboard.html')


# Define a view function for logging out
def logout_view(request):
    logout(request)
    return redirect('/login/')
