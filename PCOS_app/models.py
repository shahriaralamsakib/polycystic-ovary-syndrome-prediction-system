from django.db import models

# Create your models here.

class PolycysticOvarySyndromeModel(models.Model):
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