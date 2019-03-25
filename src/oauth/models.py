from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator, MaxValueValidator, MinValueValidator


class Farmer(models.Model):
    Income_choices = (
        ('1', 'Below 1 Lac'),
        ('2', 'Between 1 to 3 Lacs'),
        ('3', 'Above 3 Lacs'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=15, blank=True)
    farmer = models.BooleanField(default=True)
    expert = models.BooleanField(default=False)
    dob = models.DateField(blank=True)
    # aadhar_validator = RegexValidator(r'^[0-9]{12}$', message='Not a valid Aadhar  number!')
    aadhar = models.BigIntegerField(blank=True)
    img_file = models.ImageField(upload_to='media/farmers_images/', blank=True)
    land_area = models.FloatField(max_length=4, blank=True)
    registration_date = models.DateTimeField(auto_now_add=True)
    state = models.CharField(max_length=225, blank=True)
    district = models.CharField(max_length=225, blank=True)
    income = models.CharField(max_length=30, default='', blank=True, choices=Income_choices)
    major_crop = models.CharField(max_length=225, blank=True)

    """  Add location of land ....  """

    def __str__(self):
        return self.full_name


class Expert(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=15, blank=True)
    farmer = models.BooleanField(default=False)
    expert = models.BooleanField(default=True)
    dob = models.DateField(blank=True)
    registration_date = models.DateTimeField(auto_now_add=True)
    email_id = models.EmailField(max_length=254, blank=True)
    skills = models.TextField(blank=True, )
    postal_add = models.CharField(max_length=225, blank=True, )

    """ How to save image file with name of user?    """

    img_file = models.ImageField(upload_to='media/experts_images/', blank=True)

    def __str__(self):
        return self.full_name
