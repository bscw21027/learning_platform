from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser, Instructor, Student

admin.site.register(CustomUser, UserAdmin)
admin.site.register(Instructor)
admin.site.register(Student)
