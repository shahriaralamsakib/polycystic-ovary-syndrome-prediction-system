from django.http import HttpResponse
from django.shortcuts import render, redirect, redirect
from django.contrib import messages
import joblib
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth.views import login_required
from django.contrib.auth import login, logout, authenticate
from django.utils import timezone
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
            print(form.errors)
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
                return redirect('profile')
            else:
                messages.error(request, 'Invalid username or password. Please try again.')
    return render(request, 'login.html', {'form': form})

@login_required
def profile(request):

    user_predictions = PolycysticOvarySyndromeModel.objects.filter(user=request.user)

    # Pass predictions to the template context
    context = {
        'user_predictions': user_predictions
    }

    return render(request, 'profile.html', context)

@login_required
def logout_view(request):
    logout(request)
    return redirect('login_view')

# @login_required
# def pcos(request):
#     form = PCOSForm()
#     if request.method == "POST":
#         print("\033[92mPOST request received\033[0m")
#         form = PCOSForm(request.POST)
#         if form.is_valid():
#             print("\033[92mPOST request received\033[0m")
#             form_instance = form.save(commit=False)
#             form_instance.user = request.user  # Assign the current user to the form instance
#             form_instance.save()
#             folicle_no_R = form.cleaned_data['folicle_no_R']
#             folicle_no_L = form.cleaned_data['folicle_no_L']
#             cycle_r_i = form.cleaned_data['cycle_r_i']
#             cycle_len_days = form.cleaned_data['cycle_len_days']
#             amh_ng_ml = form.cleaned_data['amh_ng_ml']
#             fsh_lh = form.cleaned_data['fsh_lh']
#             prl_ng_ml = form.cleaned_data['prl_ng_ml']
#             waist_hip_ratio = form.cleaned_data['waist_hip_ratio']
#             skin_d_Y = form.cleaned_data['skin_d_Y']
#             skin_d_N = form.cleaned_data['skin_d_N']
#             hair_g_Y = form.cleaned_data['hair_g_Y']
#             hair_g_N = form.cleaned_data['hair_g_N']
#             fastFood_Y = form.cleaned_data['fastFood_Y']
#             fastFood_N = form.cleaned_data['fastFood_N']
#             weight_Y = form.cleaned_data['weight_Y']
#             weight_N = form.cleaned_data['weight_N']
#             skin_color = ''
#             if skin_d_Y == 'on':
#                 skin_color = str(1)
#             else:
#                 skin_color = str(0)

#             hair_growth = ''
#             if hair_g_Y == 'on':
#                 hair_growth = str(1)
#             else:
#                 hair_growth = str(0)

#             fast_food = ''
#             if fastFood_Y == 'on':
#                 fast_food = str(1)
#             else:
#                 fast_food = str(0)

#             weight_gain = ''
#             if weight_Y == 'on':
#                 weight_gain = str(1)
#             else:
#                 weight_gain = str(0)

#             list_data = [folicle_no_R, folicle_no_L, skin_color, hair_growth, cycle_r_i, cycle_len_days, fast_food, amh_ng_ml, fsh_lh, weight_gain, prl_ng_ml, waist_hip_ratio
#                          ]
#             data = get_output(list_data)
#             output = ''
#             if data[0] == 0:
#                 output = 'result0'
#             else:
#                 output = 'result1'
            
#             form_instance.result = output
#             form_instance.save()
#             print("Form instance saved successfully")
#             return redirect('output', output)
#         else:
#             print("\033[41mForm is not valid. Errors:", form.errors, "\033[0m")  # Red background for error message

#     return render(request, "PCOS.html", {'form': form})

@login_required
def pcos(request):
    form = PCOSForm()
    if request.method == "POST":
        print("\033[92mPOST request received\033[0m")
        form = PCOSForm(request.POST)
        if form.is_valid():
            print("\033[92mForm is valid\033[0m")
            form_instance = form.save(commit=False)
            username = request.user.username
            form_instance.user = username  # Assign the current user to the form instance
            form_instance.prediction_time = timezone.now()
            form_instance.save()

            # Extracting form data
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

            # Converting checkbox values to integers
            skin_color = 1 if skin_d_Y else 0
            hair_growth = 1 if hair_g_Y else 0
            fast_food = 1 if fastFood_Y else 0
            weight_gain = 1 if weight_Y else 0

            # Creating a list of form data
            list_data = [
                folicle_no_R, folicle_no_L, skin_color, hair_growth, cycle_r_i, cycle_len_days,
                fast_food, amh_ng_ml, fsh_lh, weight_gain, prl_ng_ml, waist_hip_ratio
            ]

            # Getting prediction
            data = get_output(list_data)
            output = 'result1' if data[0] == 1 else 'result0'
            result = 'positive' if data[0] == 1 else 'negative'  # Determine result based on output

            # Saving result and output to the form instance
            form_instance.result = result
            form_instance.save()
            print("\033[92mForm instance saved successfully\033[0m")
            return redirect('output', output)
        else:
            print("\033[41mForm is not valid. Errors:", form.errors, "\033[0m")  # Red background for error message

    return render(request, "PCOS.html", {'form': form})


def get_output(list_data):
    model = joblib.load("PCOS_app/PCOS.sav")
    prediction = model.predict([list_data])
    return prediction

@login_required
def output(request, rs):
    result = ''
    if rs == 'result0':
        result = 0
    elif rs == 'result1':
        result = 1

    return render(request, "output.html",{'result':result})