from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm

# User Registration view
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.save()
            login(request, user)
            return redirect('list_books')  # Redirect to a page after successful registration
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

# User Login view
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('list_books')  # Redirect to a page after successful login
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# User Logout view
def user_logout(request):
    logout(request)
    return render(request, 'logout.html')
