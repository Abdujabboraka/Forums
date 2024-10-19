from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from .models import Mavzu, Comment
from .forms import MavzuForm, LoginForm, RegisterForm
# Create your views here.
def  homepage(request):

    mavzu_list = Mavzu.objects.all().order_by('-created')
    context = {
        'mavzular': mavzu_list,
    }
    return render(request, 'home/index.html', context=context)


def add_mavzu(request):
    if request.method == 'POST':
        form = MavzuForm(request.POST, request.FILES)
        if form.is_valid():
            # get user id
            user_id = request.user.id

            form.instance.user_id = user_id

            form.save()
            return redirect('homepage')
    else:
        form = MavzuForm()
    return render(request, 'home/add_mavzu.html', {'form': form})

# comments
def mavzu_detail(request, pk):
    mavzu = get_object_or_404(Mavzu, id=pk)

    context = {
        'mavzu': mavzu,
        'comments': mavzu.comments.all(),
    }
    if request.method == 'POST':

        comment_text = request.POST.get('content')

        if comment_text:

            comment = mavzu.comments.create(content=comment_text, author=request.user, mavzu=mavzu)
            comment.save()
            return redirect('detail', pk=pk)

    return render(request, 'home/detail.html', context)


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect('homepage')

    else:
        form = LoginForm()

    return render(request, 'home/login.html', {'form': form})


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)  # Create the form with POST data
        if form.is_valid():
            username = form.cleaned_data['username']  # Get cleaned username

            # Check if the username already exists
            if User.objects.filter(username=username).exists():
                form.add_error('username', "Bunday foydalanuvchi nomi allaqachon mavjud")  # Add error if exists
            else:
                user = form.save(commit=False)  # Prevent immediate saving to allow for password setting
                user.set_password(form.cleaned_data['password'])  # Set the password
                user.save()  # Now save the user
                login(request, user)  # Log in the newly created user
                return redirect('homepage')  # Redirect to homepage after successful registration
    else:
        form = RegisterForm()  # Create an empty form for GET requests

    return render(request, 'home/register.html', {'form': form})
# logout the user


def logout_view(request):
    logout(request)  # Log out the user
    return redirect('homepage')  # Redirect to the homepage or a suitable page
