from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext as _

from .managers import UserManager

class User(AbstractUser):
    user_id = models.AutoField(primary_key=True,blank=True, null=False)
    email = models.EmailField(_('email address'), unique=True)
    password = models.CharField(max_length=100)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username',)

    objects = UserManager()

    def __str__(self):
        return self.email