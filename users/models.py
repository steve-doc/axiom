from django.db import models
from django.contrib.auth.models import User


# define profile model, 1-1 with user to store profile image
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(
        default='default.jpg',
        upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'
