# relationship_app/views.py
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm

# User Login view (using Django's built-in view)
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Redirect to a home page after login
    else:
        form = AuthenticationForm()
    return render(request, 'relationship_app/login.html', {'form': form})

# User Logout view (using Django's built-in view)
def logout_view(request):
    logout(request)
    return render(request, 'relationship_app/logout.html')

# User Registration view (using Django's built-in UserCreationForm)
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login page after registration
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})
