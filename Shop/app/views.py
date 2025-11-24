from pyexpat.errors import messages
from django.shortcuts import redirect, render
from django.http import HttpResponse
from . import forms
from . import models
import random
from django.contrib.auth import login

# Create your views here.
def register_view(request):
    form = forms.Login_Forms()
    if request.method == "POST":
        form = forms.Login_Forms(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            phone = form.cleaned_data.get('phone')
            user , created = models.User.objects.get_or_create(username=phone, defaults={'first_name': name})
            
            models.Product.objects.update_or_create(
                user=user,
                defaults={"name": name, "phone": phone}
            )

            code = str(random.randint(1000, 9999))
            models.OTP.objects.update_or_create(user=user, defaults={"code": code})
            
            print("=== OTP GENERATED ===")
            print("USER:", phone)
            print("OTP:", code)
            print("=====================")

            messages.success(request, f"کد تایید ارسال شد: {code}")
            request.session['otp_user'] = user.id
            return redirect('login')

    context = {'form': form}
    return render(request, 'login_register.html', context)


def login_view(request):
    user_id = request.session.get("otp_user")
    if not user_id:
        messages.error(request, "دسترسی نامعتبر است.")
        return redirect("register")
    
    user = models.User.objects.get(id=user_id)
    otp_obj = models.OTP.objects.get(user=user)

    form = forms.OTPForm()

    if request.method == "POST":
        form = forms.OTPForm(request.POST)
        if form.is_valid():  # اصلاح شد
            code = form.cleaned_data.get("code")

            print("=== USER ENTERED CODE ===")
            print("expected:", otp_obj.code)
            print("entered :", code)
            print("=========================")

            if code == otp_obj.code:
                login(request, user)
                messages.success(request, "با موفقیت وارد شدید.")
                otp_obj.delete()
                del request.session['otp_user']

                return redirect("home")

            messages.error(request, "کد وارد شده اشتباه است.")

    return render(request, "login.html", {"form": form, "phone": user.username})
