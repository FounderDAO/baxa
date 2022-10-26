from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
from rest_framework import serializers
from apps.core.models import Language, Gender, Status, MemberType


class Country(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    sort_number = models.IntegerField(default=0)
    status = models.IntegerField(choices=Status.choices, default=Status.NEW)

    def __str__(self):
        return self.name


class Region(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    sort_number = models.IntegerField(default=0)
    status = models.IntegerField(choices=Status.choices, default=Status.NEW)

    def __str__(self):
        return self.name


class District(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    sort_number = models.IntegerField(default=0)
    status = models.IntegerField(choices=Status.choices, default=Status.NEW)

    def __str__(self):
        return self.name


class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not username:
            raise ValueError('Users must have an username')
        user = self.model(
            username=username,
        )
        user.set_password(password)
        user.email = email
        user.save()
        user_serializer = ProfileSerializer(data={'user': user.id})
        if user_serializer.is_valid():
            user_serializer.save()
        return user

    def create_staffuser(self, username, email, password):
        if not password:
            raise ValueError('staff/admins must have a password.')
        user = self.create_user(username, email, password=password)
        user.is_staff = True
        user.save()
        return user

    def create_superuser(self, username, email, password=None):
        if not password:
            raise ValueError('superusers must have a password.')
        user = self.create_user(username, email, password=password)
        user.username = username
        user.email = email
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user


class User(AbstractUser):
    username = models.CharField(max_length=254, unique=True)  # shu ishlamasaxam turishi kerak ekan
    email = models.EmailField(max_length=254, unique=True)
    activate_date = models.DateTimeField(auto_now_add=True)
    language = models.IntegerField(choices=Language.choices, default=Language.UZBEK)
    password = models.CharField(max_length=100)
    status = models.IntegerField(choices=Status.choices, default=Status.NEW)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    def __str__(self):
        return self.username


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, blank=True, null=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, blank=True, null=True)
    district = models.ForeignKey(District, on_delete=models.CASCADE, blank=True, null=True)
    phone_number = models.CharField(max_length=25, blank=True, null=True)
    home_number = models.CharField(max_length=25, blank=True, null=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    midd_name = models.CharField(max_length=100, blank=True, null=True)
    brith_date = models.DateField(blank=True, null=True)
    gender = models.IntegerField(choices=Gender.choices, blank=True, null=True)
    type = models.IntegerField(choices=MemberType.choices, default=MemberType.GUEST)


class Image(models.Model):
    name = models.CharField(max_length=220)
    file = models.CharField(max_length=220)
    status = models.IntegerField(choices=Status.choices, default=Status.NEW)

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'