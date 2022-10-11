from django.db import models

from apps.accounts.models import User, Country, Region, District
from apps.core.models import Status


class Category(models.Model):
    parent = models.ForeignKey('Category', on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=30)
    description = models.TextField()
    sort_number = models.IntegerField(default=0)
    status = models.IntegerField(choices=Status.choices, default=Status.NEW)

    def __str__(self):
        return self.name


class Type(models.Model):
    name = models.CharField(max_length=220)
    description = models.TextField()
    sort_number = models.IntegerField()
    status = models.IntegerField(choices=Status.choices, default=Status.NEW)


class Days(models.IntegerChoices):
    Monday = 1
    Tuesday = 2
    Wednesday = 3
    Thursday = 4
    Friday = 5
    Saturday = 6
    Sunday = 7


class SubscribeType(models.IntegerChoices):
    DEFAULT = 1
    SILVER = 2
    GOLD = 3
    PREMIUM = 4
    DIAMOND = 5


class Service(models.Model):
    name = models.CharField(max_length=220)
    description = models.TextField()
    latitude = models.CharField(max_length=12, blank=True, null=True)
    longitude = models.CharField(max_length=12, blank=True, null=True)
    phone_number = models.CharField(max_length=30)
    address = models.CharField(max_length=220)
    service_phone_number = models.CharField(max_length=30)  # for us
    logo = models.FileField(upload_to="service_logos", blank=True, null=True)
    rank = models.FloatField(default=0.0)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner', blank=True, null=True)
    type = models.IntegerField(choices=SubscribeType.choices, default=SubscribeType.DEFAULT)
    is_premium = models.BooleanField(default=False)
    sort_number = models.IntegerField(default=0)
    view_count = models.IntegerField(default=0)
    status = models.IntegerField(choices=Status.choices, default=Status.NEW)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "service"
        verbose_name_plural = "Service"


class ServiceImage(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, blank=True, null=True)
    file = models.ImageField(upload_to='service_image')
    status = models.IntegerField(choices=Status.choices, default=Status.NEW)
    sort_number = models.IntegerField(default=0)

    def __str__(self):
        return self.file.url


class WorkingDay(models.Model):
    day = models.IntegerField(choices=Days.choices)
    work_start = models.DateTimeField()
    work_end = models.DateTimeField()
    launch_start = models.DateTimeField()
    launch_end = models.DateTimeField()


class Comment(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    parent = models.ForeignKey('Comment', on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    rank = models.FloatField(default=0)
    status = models.IntegerField(choices=Status.choices, default=Status.ACTIVE)

    def __str__(self):
        return self.description


class CommentImage(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    file = models.FileField()
    status = models.IntegerField(choices=Status.choices, default=Status.NEW)
