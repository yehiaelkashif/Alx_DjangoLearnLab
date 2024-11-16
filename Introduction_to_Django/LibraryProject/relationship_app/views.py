from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from .views import check_role



def check_role(user, role):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == role

@user_passes_test(lambda u: check_role(u, 'Librarian'))
def librarian_dashboard(request):
    return render(request, 'librarian_dashboard.html', {'message': 'Welcome, Librarian!'})

from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from .views import check_role

@user_passes_test(lambda u: check_role(u, 'Member'))
def member_dashboard(request):
    return render(request, 'member_dashboard.html', {'message': 'Welcome, Member!'})
