from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _

from users.managers import YamdbUserManager

ROLES = (("user", "user"), ("moderator", "moderator"), ("admin", "admin"))


class YamdbUser(AbstractUser):
    email = models.EmailField(_("email address"), unique=True)
    bio = models.TextField(blank=True, null=True)
    role = models.CharField(choices=ROLES, default='user', max_length=10)
    confirmation_code = models.CharField(max_length=255, blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = YamdbUserManager()
