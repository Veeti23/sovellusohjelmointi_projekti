from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required

def register(request):
    # Register a new user.
    if request.method != 'POST':
       #display blank registration form.
       form = UserCreationForm()
    else:
        # process input from data
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            # Log the user in and redirect to home page.
            login
            return redirect('verkkokauppa:home')
    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'registration/register.html', context)