from django.db import models

# Custom Imports
from django.contrib.auth import get_user_model

# Default User
User = get_user_model()

# Model to store the Details of the user
class UserDetails(models.Model):

    # Foreign key to the Default User of Django
    user = models.ForeignKey(User, on_delete=models.CASCADE, null = True, blank = True)

    # College
    college = models.CharField(max_length = 255, blank = True, null = True)
    # Further Details of the user can be added here

    class Meta:
        verbose_name = 'User Detail'
        verbose_name_plural = 'User Details'