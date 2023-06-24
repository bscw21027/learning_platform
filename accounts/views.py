from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm

def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.user_type = form.cleaned_data['user_type']
            user.save()
            return redirect('accounts:login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect the user to their respective dashboard
                if user.user_type == 'instructor':
                    return redirect('accounts:instructor_dashboard')
                elif user.user_type == 'student':
                    return redirect('accounts:student_dashboard')
    else:
        form = AuthenticationForm()

    return render(request, 'accounts/login.html', {'form': form})


def home_view(request):
    return render(request, 'accounts/home.html')


def instructor_dashboard(request):
    # Add your instructor dashboard logic here
    return render(request, 'accounts/instructor_dashboard.html')


def student_dashboard(request):
    # Add your student dashboard logic here
    return render(request, 'accounts/student_dashboard.html')
