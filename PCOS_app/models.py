from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

class PolycysticOvarySyndromeModel(models.Model):
    user = models.CharField(max_length=150)
    # Add fields for medical data
    prediction_time =models.DateTimeField(default=timezone.now) 
    folicle_no_R = models.CharField(max_length=50, blank=False, null=False)
    folicle_no_L = models.CharField(max_length=50, blank=False, null=False)
    cycle_r_i = models.CharField(max_length=50, blank=False, null=False)
    cycle_len_days = models.CharField(max_length=50, blank=False, null=False)
    amh_ng_ml = models.CharField(max_length=50, blank=False, null=False)
    fsh_lh = models.CharField(max_length=50, blank=False, null=False)
    prl_ng_ml = models.CharField(max_length=50, blank=False, null=False)
    waist_hip_ratio = models.CharField(max_length=50, blank=False, null=False)
    skin_d_Y = models.BooleanField(default=False)
    skin_d_N = models.BooleanField(default=False)
    hair_g_Y = models.BooleanField(default=False)
    hair_g_N = models.BooleanField(default=False)
    fastFood_Y = models.BooleanField(default=False)
    fastFood_N = models.BooleanField(default=False)
    weight_Y = models.BooleanField(default=False)
    weight_N = models.BooleanField(default=False)
    # Add other fields for medical data as needed
    result = models.CharField(max_length=50, blank=True, null=True)

    # def __str__(self):
    #     return f'Medical Data for {self.user.username}'
