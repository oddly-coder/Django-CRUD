from django.shortcuts import render, redirect
from .forms import RegisterationForm
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form  = RegisterationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'An account has been created for {username}')
            return redirect('blog-home')

    form  = RegisterationForm()
    return render(request, "register.html", {"form":form})
