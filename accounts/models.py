from django.contrib.auth.models import AbstractUser

from django.db import models


class user(AbstractUser):

    username = None

    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, blank=True)
    
    ACCOUNT_TYPE_CHOICES = (
        ('personal', 'Personal'),
        ('mentorship', 'Mentorship'),
    )
    account_type = models.CharField(
        max_length=20,
        choices=ACCOUNT_TYPE_CHOICES,
        default='personal'
    )

    career_level = models.CharField(max_length=100, blank=True)
    interests = models.TextField(blank=True)
    profile_image = models.ImageField(
        upload_to='profiles/',
        blank=True,
        null=True
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email