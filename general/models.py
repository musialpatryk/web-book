from django.db import models


class AbstractEntity(models.Model):
    id = models.AutoField(primary_key=True)
    created = models.DateTimeField(auto_created=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
