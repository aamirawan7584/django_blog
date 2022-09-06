from django.shortcuts import render,redirect
from django.contrib import messages
from users.forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Your Account has been created! You can now Login')
            return redirect('login')
            
    else:
        form = UserRegisterForm()
    return render(request=request,template_name='users/register.html',context={'form':form})

@login_required
def profile(request):
    return render(request=request,template_name="users/profile.html")

