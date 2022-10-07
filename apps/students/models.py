from django.core.validators import RegexValidator
from django.db import models
from django.urls import reverse
from django.utils import timezone

from apps.corecode.models import StudentClass
import random


class Student(models.Model):
    STATUS_CHOICES = [("active", "Active"), ("inactive", "Inactive")]

    GENDER_CHOICES = [("male", "Male"), ("female", "Female")]

    # current_status = models.CharField(
    #     max_length=10, choices=STATUS_CHOICES, default="active"
    # )
    # registration_number = models.CharField(max_length=200, unique=True)
    # surname = models.CharField(max_length=200)




    full_Name = models.CharField(max_length=200)
    parents_Or_Guardian = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=200, blank=True)
    state = models.CharField(max_length=200, blank=True)
    # gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default="male")
    date_of_birth = models.DateField(default=timezone.now)
    disability = models.CharField(max_length=200, blank=True)


    # disability = random.choice(["Yes", "No"])
    num_users = models.IntegerField()


    # full_Name = models.CharField(max_length=200, blank=True, null=True)
    # parent_Or_Guardian = models.CharField(max_length=200, blank=True, null=True)
    # # other_name = models.CharField(max_length=200, blank=True)
    # # DOB = models.CharField(max_length=10, choices=GENDER_CHOICES, default="male")
    # DOB = models.DateField(default=timezone.now)
    # State = models.CharField(max_length=200, blank=True, null=True, default=None)
    # Disability = random.choice(["Yes", "No"])
    # # State = models.ForeignKey(
    # #     StudentClass, on_delete=models.SET_NULL, blank=True, null=True
    # # )
    # # date_of_admission = models.DateField(default=timezone.now)

    # # mobile_num_regex = RegexValidator(
    # #     regex="^[0-9]{10,15}$", message="Entered mobile number isn't in a right format!"
    # # )
    # # parent_mobile_number = models.CharField(
    # #     validators=[mobile_num_regex], max_length=13, blank=True
    # # )

    # City = models.CharField(max_length=200, null=True)


    # current_class = models.ForeignKey(
    #     StudentClass, on_delete=models.SET_NULL, blank=True, null=True
    # )
    # date_of_admission = models.DateField(default=timezone.now)

    # mobile_num_regex = RegexValidator(
    #     regex="^[0-9]{10,15}$", message="Entered mobile number isn't in a right format!"
    # )
    # parent_mobile_number = models.CharField(
    #     validators=[mobile_num_regex], max_length=13, blank=True
    # )

    # address = models.TextField(blank=True)
    # others = models.TextField(blank=True)
    # passport = models.ImageField(blank=True, upload_to="students/passports/")

    # class Meta:
    #     ordering = ["", "full_Name", "other_name"]

    def __str__(self):
        return "{}-{}".format(self.full_Name, self.disability)

    # def __str__(self):
    #     return f"{self.surname} {self.full_Name} {self.other_name} ({self.registration_number})"

    def get_absolute_url(self):
        return reverse("student-detail", kwargs={"pk": self.pk})


class StudentBulkUpload(models.Model):
    date_uploaded = models.DateTimeField(auto_now=True)
    csv_file = models.FileField(upload_to="students/bulkupload/")


