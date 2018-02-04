# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Account(models.Model):
    # Look into, may need for auth, will need to import auth
    #user = models.OneToOneField(User)

    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone_number = models.IntegerField(null=True)

    class Meta:
        db_table = 'account_table'