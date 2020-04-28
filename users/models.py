from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

from users.managers import YamdbUserManager

ROLES = (('user', 'user'), ('moderator', 'moderator'), ('admin', 'admin'))

class YamdbUser(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    bio = models.TextField(blank=True, null=True)
    role = models.CharField(choices=ROLES, default='user', max_length=10)

    objects = YamdbUserManager()

