from django.db import models
from django.contrib.auth.models import User



# User Modelo
class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    name_owner = models.CharField(max_length=150)
    phone = models.IntegerField()
    email = models.CharField(max_length=200)
    id_owner = models.IntegerField()

    def __str__(self) -> str:
        return str(self.user_id)


# Pet Model
class Pet(models.Model):
    pet_id = models.AutoField(primary_key=True)
    pet_name = models.CharField(max_length=150)
    pet_type = models.CharField(max_length=150)
    pet_age = models.IntegerField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.pet_name


# Groomings Type model
class Grooming(models.Model):
    grooming_id = models.AutoField(primary_key=True)
    grooming_name = models.CharField(max_length=150)
    duration = models.FloatField()

    def __str__(self):
        return self.grooming_name


# Grooming reservation model
class Reservation(models.Model):
    reservation_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    pet_id = models.ForeignKey(Pet, on_delete=models.CASCADE)
    grooming_id = models.ForeignKey(Grooming, on_delete=models.CASCADE)
    date = models.DateField()
    hours = models.IntegerField()

    def __str__(self):
        return str(self.reservation_id)


# Availability schedule model
class Availability(models.Model):
    availability_id = models.AutoField(primary_key=True)
    date = models.DateField()
    hour_start = models.IntegerField()
    hour_end = models.IntegerField()

    def __str__(self):
        return str(self.availability_id)


# Schedule model
class Schedule(models.Model):
    schedule_id = models.AutoField(primary_key=True)
    available_dates = models.DateField()
    available_hours = models.IntegerField()
    availability_id = models.ForeignKey(Availability, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.schedule_id)


# Events model
class Event(models.Model):
    event_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return str(self.name)