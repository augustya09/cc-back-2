import uuid
from django.db import models

# create your models here 

class BaseModel(models.Model):
    """
    Abstract base class inherited by every real model in this project.
    UUID primary key instead of Django's default auto-incrementing integer:
    sequential IDs let anyone enumerate the API by guessing /api/tasks/4/, /5/...
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True