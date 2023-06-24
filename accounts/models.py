from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = [
        ('instructor', 'Instructor'),
        ('student', 'Student'),
    ]
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES, default='student')
    
    class Meta:
        # Add this meta option to resolve the clash
        swappable = 'AUTH_USER_MODEL'


class Instructor(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    # Add any additional fields specific to instructors
    bio = models.TextField()

    def __str__(self):
        return self.user.username


class Student(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    # Add any additional fields specific to students
    graduation_year = models.IntegerField()

    def __str__(self):
        return self.user.username
