from django.db import models

class Schedule(models.Model):
    password = models.CharField(max_length=20, unique=True)

class Event(models.Model):
    schedule = models.ForeignKey(Schedule, related_name='events', on_delete=models.CASCADE)
    when = models.CharField(max_length=100)
    where = models.CharField(max_length=100)
    who = models.CharField(max_length=100)