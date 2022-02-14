from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.core.validators import MaxValueValidator, MinValueValidator

class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self, email, name, password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError('Users must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name,)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """Create and save a new superuser with given details"""
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return userr

class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Retrieve full name for user"""
        return self.name

    def get_short_name(self):
        """Retrieve short name of user"""
        return self.name

    def __str__(self):
        """Return string representation of user"""
        return self.email

class Category(models.Model):
    id =  models.IntegerField(primary_key= True)
    name = models.CharField(max_length = 100)

class Course(models.Model):
    id =  models.IntegerField(primary_key= True)
    category_id = models.ForeignKey(Category,null=True, on_delete = models.SET_NULL)
    name = models.CharField(max_length = 150)
    details = models.CharField(max_length =1000)
    price = models.IntegerField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    language = models.CharField(max_length =50)


class CourseImage(models.Model):
     id = models.IntegerField(primary_key= True)
     image_path = models.TextField()
     course_id = models.ForeignKey(Course, null=True , on_delete=models.SET_NULL)


class CourseVideo(models.Model):
     id = models.IntegerField(primary_key= True)
     video_path = models.TextField()
     course_id = models.ForeignKey(Course, null=True , on_delete=models.SET_NULL)
     name = models.CharField(max_length=100)
     description = models.TextField()


class Insturctor(models.Model):
    id = models.IntegerField(primary_key= True)
    name = models.CharField(max_length=100)
    image = models.TextField()
    description = models.TextField()

    rate = models.IntegerField(
        default=0,
        validators=[ MaxValueValidator(8),MinValueValidator(1)]
    )

class CourseInstructor(models.Model):
    instructor_id = models.ForeignKey(Insturctor, null=True , on_delete=models.SET_NULL)
    course_id = models.ForeignKey(Course, null=True ,on_delete=models.SET_NULL)


class Articles(models.Model):
    name = models.CharField(max_length=100)
    text = models.TextField()


class Partner(models.Model):
    name = models.CharField(max_length=150)
    logo = models.FileField(upload_to="logos", max_length=100)
