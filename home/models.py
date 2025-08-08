# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    retirar dinero instantaneo = models.CharField(max_length=255, null=True, blank=True)
     bank yape generador retiros de dineros por  numero = models.TextField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class App Yape(models.Model):

    #__App Yape_FIELDS__
    bank yape = models.TextField(max_length=255, null=True, blank=True)
    yape bank = models.CharField(max_length=255, null=True, blank=True)

    #__App Yape_FIELDS__END

    class Meta:
        verbose_name        = _("App Yape")
        verbose_name_plural = _("App Yape")



#__MODELS__END
