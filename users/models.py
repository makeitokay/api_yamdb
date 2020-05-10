from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _

from users.managers import YamdbUserManager


class YamdbUser(AbstractUser):
    email = models.EmailField(_("email address"), unique=True)
    ROLES = (("user", "user"), ("moderator", "moderator"), ("admin", "admin"))
    bio = models.TextField(blank=True, null=True)
    role = models.CharField(choices=ROLES, default="user", max_length=10)
    confirmation_code = models.CharField(max_length=255, blank=True, null=True)

    objects = YamdbUserManager()
