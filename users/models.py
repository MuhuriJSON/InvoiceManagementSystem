# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import AbstractUser
from django.db import models
# Create your models here.

auth_level = [
    ("SELECT", "Select"),
    ("ADMIN", "Admin"),
    ("REGULAR", "Regular"),
]


class User(AbstractUser):

    def __unicode__(self):
        return self.username
