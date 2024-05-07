from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
import joblib
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth.views import login_required
from django.contrib.auth import login, logout, authenticate
import pandas as pd
import pickle

# Create your views here.


# def register(request):
#     form = RegistrationForm()
#     if request.method == "POST":
#         form = RegistrationForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
            
#             # Check if the username already exists
#             if User.objects.filter(username=username).exists():
#                 messages.error(request, 'Username already exists. Please choose a different username.')
#             else:
#                 form.save()
#                 messages.success(request, 'Registration successful. You can now log in.')
#                 return redirect('login_view')
#         error_messages = [message for message in messages.get_messages(request) if message.level == messages.ERROR]
#         success_messages = [message for message in messages.get_messages(request) if message.level == messages.SUCCESS]
#         print(error_messages)
#         print(success_messages)

#     return render(request, "registration.html", {'form': form})
def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful. You can now log in.')
            return redirect('login_view')
        else:
            messages.error(request, 'Registration failed. Invalid Information or Password')
    else:
        form = RegistrationForm()

    return render(request, "registration.html", {'form': form})

def login_view(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        us = request.POST['username']
        ps = request.POST['password']
        if us is not None and ps is not None:
            user = authenticate(request, username=us, password=ps)
            if user:
                login(request, user)
                return redirect('pcos')
            else:
                messages.error(request, 'Invalid username or password. Please try again.')
    return render(request, 'login.html', {'form': form})

def logout_form(request):
    logout(request)
    return HttpResponseRedirect('')

def pcos(request):
    form = PCOSForm()
    if request.method == "POST":
        form = PCOSForm(request.POST)
        if form.is_valid():
            form.save()
            folicle_no_R = form.cleaned_data['folicle_no_R']
            folicle_no_L = form.cleaned_data['folicle_no_L']
            cycle_r_i = form.cleaned_data['cycle_r_i']
            cycle_len_days = form.cleaned_data['cycle_len_days']
            amh_ng_ml = form.cleaned_data['amh_ng_ml']
            fsh_lh = form.cleaned_data['fsh_lh']
            prl_ng_ml = form.cleaned_data['prl_ng_ml']
            waist_hip_ratio = form.cleaned_data['waist_hip_ratio']
            skin_d_Y = form.cleaned_data['skin_d_Y']
            skin_d_N = form.cleaned_data['skin_d_N']
            hair_g_Y = form.cleaned_data['hair_g_Y']
            hair_g_N = form.cleaned_data['hair_g_N']
            fastFood_Y = form.cleaned_data['fastFood_Y']
            fastFood_N = form.cleaned_data['fastFood_N']
            weight_Y = form.cleaned_data['weight_Y']
            weight_N = form.cleaned_data['weight_N']
            skin_color = ''
            if skin_d_Y == 'on':
                skin_color = str(1)
            else:
                skin_color = str(0)

            hair_growth = ''
            if hair_g_Y == 'on':
                hair_growth = str(1)
            else:
                hair_growth = str(0)

            fast_food = ''
            if fastFood_Y == 'on':
                fast_food = str(1)
            else:
                fast_food = str(0)

            weight_gain = ''
            if weight_Y == 'on':
                weight_gain = str(1)
            else:
                weight_gain = str(0)

            list_data = [folicle_no_R, folicle_no_L, skin_color, hair_growth, cycle_r_i, cycle_len_days, fast_food, amh_ng_ml, fsh_lh, weight_gain, prl_ng_ml, waist_hip_ratio
                         ]
            data = get_output(list_data)
            output = ''
            if data[0] == 0:
                output = 'result0'
            else:
                output = 'result1'
            return redirect('output', output)
    return render(request, "PCOS.html", {'form': form})

def get_output(list_data):
    model = joblib.load("PCOS_app/PCOS.sav")
    prediction = model.predict([list_data])
    return prediction

def output(request, rs):
    result = ''
    if rs == 'result0':
        result = 0
    elif rs == 'result1':
        result = 1

    return render(request, "output.html",{'result':result})