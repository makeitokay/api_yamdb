from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db import models
from django.utils.translation import ugettext_lazy as _

from api.users.managers import YamdbUserManager


class YamdbUser(AbstractUser):
    email = models.EmailField(_("email address"), unique=True)
    ROLES = (("user", "user"), ("moderator", "moderator"), ("admin", "admin"))
    bio = models.TextField(_("biography"), blank=True, null=True)
    role = models.CharField(
        _("role"),
        choices=ROLES,
        default="user",
        max_length=10
    )

    objects = YamdbUserManager()


class UserConfirmationCode(models.Model):
    user = models.OneToOneField(
        "YamdbUser",
        models.CASCADE,
        related_name="confirmation_code"
    )
    code = models.CharField(max_length=255, blank=True, null=True)
