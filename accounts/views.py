from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Create your views here.
def register_view(request):
    form = UserCreationForm(request.POST or None)
    context = {
        "form": form,
    }
    if form.is_valid():
        user_obj = form.save()
        return redirect('/login/')
    
    return render(request, 'accounts/register.html', context=context)
    
def login_view(request):
    form = AuthenticationForm(request, data=request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
        
    context = {
        "form": form,
    }
    return render(request, 'accounts/login.html', context=context)

def logout_view(request):
    # context = {}
    if request.method == "POST":
        logout(request) 
        return redirect('/login/')
    
    return render(request, 'accounts/logout.html', {})

 