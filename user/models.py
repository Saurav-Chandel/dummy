import datetime

from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.utils.timezone import now
# from app import choices

# Create your models here.
TOKEN_TYPE_CHOICES = (
    ("verification", "Email Verification"),
    ("pwd_reset", "Password Reset"),
)

class AppUserManager(UserManager):
    # def get_by_natural_key(self, username):
    #     return self.get(email__iexact=username)

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def _create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """
        Create a Super Admin. Not to be used by any API. Only used for django-admin command.
        :param email:
        :param password:
        :param extra_fields:
        :return:
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault('is_active', True)

        user = self._create_user(email, password, **extra_fields)
        return user


class User(AbstractUser):
    first_name = models.CharField(
        max_length=200, default=None, null=True, blank=True
    )
    last_name = models.CharField(
        max_length=200, default=None, null=True, blank=True
    )
    email=models.EmailField(unique=True,null=False)

    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    manager = AppUserManager()

    def __str__(self):
        return self.first_name        


class Token(models.Model):
    token = models.CharField(max_length=300)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    token_type = models.CharField(
        max_length=20, choices=TOKEN_TYPE_CHOICES
    )
    created_on = models.DateTimeField(default=now, null=True, blank=True)
    expired_on = models.DateTimeField(default=now, null=True, blank=True)


class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to ='media',null=True,blank=True)
    city=models.CharField(max_length=100,blank=True,null=True)
    state=models.CharField(max_length=100,blank=True,null=True)
    zip_code=models.CharField(max_length=100,blank=True,null=True)
    cpf_number=models.IntegerField(unique=True)

    # def __str__(self):
    #     return self.state









