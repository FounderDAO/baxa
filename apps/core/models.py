from django.db import models


class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)


class Language(models.IntegerChoices):
    UZBEK = 1
    RUSSIAN = 2
    ENGLISH = 3
    TURKEY = 4


class Gender(models.IntegerChoices):
    MALE = 1
    FEMALE = 2
    OTHER = 3


class MemberType(models.IntegerChoices):
    AUTHOR = 1
    OWNER = 2
    GUEST = 3


class Status(models.IntegerChoices):
    NEW = 1
    IN_APPROVED = 2
    ACTIVE = 3
    FROZEN = 4
    DELETED = 5
