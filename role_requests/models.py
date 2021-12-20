from django.db import models
from general.models import AbstractEntity
from django.db import models
from django.contrib.auth.models import User

class RoleRequestManager(models.Manager):
    def create_role_request(
            self,
            message,
            user
    ):
        return self.create(
            message = message,
            user = user
        )


# Create your models here.
class RoleRequest(AbstractEntity):

    objects = RoleRequestManager()

    STATUS_PENDING = 0
    STATUS_REJECTED = 1
    STATUS_ACCEPTED = 2

    ROLE_REQUEST_ADMIN = 0

    user = models.ForeignKey(User, on_delete = models.CASCADE)
    message = models.CharField(max_length = 200, default = "None")
    role_request = models.IntegerField(default = ROLE_REQUEST_ADMIN)
    status = models.IntegerField(default = STATUS_PENDING)