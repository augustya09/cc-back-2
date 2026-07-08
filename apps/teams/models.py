from django.db import models
from django.conf import settings

# Create your models here.

class Team(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Membership(models.Model):
    ROLE_CHOICES = (
        ('OWNER','Owner'),
        ('MAINTAINER', 'Maintainer'),
        ('MEMBER', 'Member'),
        ('VIEWER','Viewer')
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='memberships')
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    joined_at = models.DateTimeField(auto_now_add=True)

    class Meta: # pass metadata settings to the model that dont represent actual table coloumns
        unique_together = ('user', 'team') #prevents user from being added to the same team more than once
