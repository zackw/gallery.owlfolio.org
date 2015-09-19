from django.db import models
from django.contrib.auth.models import User

import uuid

class AutoLogin(models.Model):
    user = models.ForeignKey(User)
    token = models.UUIDField(primary_key=True, default=uuid.uuid4)

    def __str__(self):
        return self.user.get_username()