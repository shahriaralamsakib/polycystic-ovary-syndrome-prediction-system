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

def research(request):
    pdf_url = "https://pdf.sciencedirectassets.com/312075/1-s2.0-S2352914824X00039/1-s2.0-S235291482400056X/main.pdf?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLWVhc3QtMSJGMEQCIBm%2Fx3OuC9eBXeAoU5NLCdcpIpXAklvbavoxlMr0aoBpAiASFiB8sb1cXGjjBnDSTp7ahNsZUMCDieQ2ezQxbv9eISq7BQjB%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAUaDDA1OTAwMzU0Njg2NSIM0oF7P1kJ0WSL%2B1LXKo8FjpLgAjZOwdhiesUTXCqJ0%2Bp%2FkrEgy0WXQdusiNSaqR8qqX2%2B%2Fl9pTX0uSx1q%2FuqFxewBOmb%2BlmGoKZH3Qf0M74K94aWzX4vwPIWrzLR5sHrEybIsQpGpoKym8RcGL%2BzX1WZmlqwm9f204YazJ3DdzBaoj6OpF9zU%2FLGyHy%2FhLK1392OtoNJo5swYaI2%2FKr4zvl972gwFiLtoincXswwq6K%2B8GqFETmQ4G6bnInieCIBOU0cY%2BytjCKWPSTZtzojDgLvfh8T2%2Fl8R6P2URnccUhRpw9fNgp%2Ft38%2BTnhbGT%2B3h2M28yqIEaSR9oml0bvosXDBElPpV%2FfC5b0iQxtMnniVldt6lBtpph87DG6Bcpom9UoIj3tGhOJzuSGonQCI4yEzHIVjow3VOOptdTSH44pWQT3ZvJrJppkkDjrOE6XUfio53Cwf9Q%2FvJ7pX%2BLYrBO7QyEfmN5Ylrab%2FZqRJYrmp5VSwk6h5qeOaO5fJNU40pfx6X265Ejxd9o08mc8A9A8XJVmDgONoJJA9XKiIoavXZk66ANzmBrNGHk3sFkV08c7EVT8KxK3%2Fv8%2F%2FVYtaR5NMEZ7PK8mtAUXyzVjjB5JMsv2mBfE7XcYgyQDE49kBqqBYcvxdZ1FKdvw7X49rQ2mTFm8Lv%2F%2BRwhwl0V2sd8dy9ViMn2%2Fz7iO9ntyQO1nwkbtEHKAbPea%2FDvtIvxhg%2BjUy7sjuKlKOX3Iduyye9ae%2FzEweZuv%2FrqMTeiNrcxk0eBDSaapxOt2WtqBYZO4DYtY1p9LslLC6DMFv2N48b7rKxWhZaPlVDp4oJyojyUeITV5VL3RKcRjGc%2BRlbC2BtAAHQMX8%2FCXIZ7zC406D9Mn44DA2XePNtiDL%2BJkrCCzDCwuuzBjqyAXau00jRtkFdg4uayq1E1JhM4WWxSho6lk7SvjIuGshjrMAvBSwyEwd1c1XNtAlmiWONOMV3q3DraHumuOCrQcM%2BzY3dZIZtrqWDcmwMYp7Ua5Dh4NFth8%2Bgp%2B%2Fezr6QGSbQVSBmNaQwRpI4Pu0oHF3anyqtqLGEcdYiQOuRIYlqm5HgX6KmBm116g0tGxq3vBDYgQx5i7ruzwHxsDKw9DpmMTB%2BellgXxTkUM3ns47%2Bbj8%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20240625T162734Z&X-Amz-SignedHeaders=host&X-Amz-Expires=300&X-Amz-Credential=ASIAQ3PHCVTYZYZBGPVK%2F20240625%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=b2441fcf77889631cd1a008abe9201d739ca45d1105aae5e482ee9750de28a0e&hash=8fd9ca581a9dc842e776c91d0b7c85b79305783747874678d043e700304976ae&host=68042c943591013ac2b2430a89b270f6af2c76d8dfd086a07176afe7c76c2c61&pii=S235291482400056X&tid=spdf-516a5df1-75e6-49b6-a360-63c7a2aca230&sid=6c422fdd329e464b74188937ecf1ea08a016gxrqb&type=client&tsoh=d3d3LnNjaWVuY2VkaXJlY3QuY29t&ua=00025c5e5e505a5453&rr=899653650ff2b252&cc=bd"
    return render(request, 'research.html', {'pdf_url': pdf_url})

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