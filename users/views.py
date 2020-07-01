from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout


from .forms import CreateUserForm
from .decorators import unauthenticated_user

@unauthenticated_user
def signup(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CreateUserForm()
    return render(request, 'registration/signup.html', {
        'form': form
    })