from pyexpat.errors import messages
from django.shortcuts import redirect, render
from django.http import HttpResponse
from . import forms
from . import models
import random

# Create your views here.
def register_view(request):
    if request.method == "POST":
        form = forms.Login_Forms(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            phone = form.cleaned_data.get('phone')
            user , created = models.User.objects.get_or_create(username = phone , defaults={'first_name': name})
            
            models.Product.objects.update_or_create(
                user = user ,
                defaults={"name": name , "phone":phone}
            )
            
            #generate_OTPCode
            code = str(random.randint(1000 , 9999))
            models.OTP.objects.update_or_create(user = user , defaults={"code": code})  
            
            messages.success(request, f"کد تایید ارسال شد: {code}")  
            request.session['otp_user'] = user.id
            return redirect('login')
        else:
            form = forms.Login_Forms()
        
    context = {
        'form': form
    }
            
    return render(request, 'login_register.html', context)


def login_view(request):
    user_id = request.session.get("otp_user")
    if not user_id:
        messages.error(request, "دسترسی نامعتبر است.")
        return redirect("register")
    
    
