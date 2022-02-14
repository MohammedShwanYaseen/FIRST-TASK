from django.contrib import admin
from profiles_api import models

admin.site.register(models.UserProfile)
admin.site.register(models.Category)
admin.site.register(models.Course)
admin.site.register(models.CourseImage)
admin.site.register(models.CourseVideo)
admin.site.register(models.Articles)
admin.site.register(models.Insturctor)
admin.site.register(models.Partner)

# Register your models here.
