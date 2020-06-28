# from django.db import models
# from django.contrib.auth.models import AbstractUser
#
# # Create your models here.
# class User(AbstractUser):
#     is_emp = models.BooleanField(default=False)
#     is_client = models.BooleanField(default=False)
#
#     def __str__(self):
#         self.username
#
# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
#     location = models.CharField(max_length=264)
#     profile_pic = models.ImageField((upload_to='profile_pics', blank=True))
