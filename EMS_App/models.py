from django.db import models

# Create your models here.
from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=122,null=True)
    email = models.CharField(max_length=122,null=True)
    phone = models.CharField(max_length=12,null=True)
    desc = models.TextField(null=True)
    date = models.DateField(null=True)
    
    def __str__(self):
        return self.name
    

class EventAdvisor(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    destination = models.CharField(max_length=122)
    date = models.DateField(null=True)
    time = models.TimeField(null=True)
    desc = models.TextField(max_length=500,null=True)
    guest = models.CharField(max_length=500,null=True)


    def __str__(self):
        return self.name
    

class CollegeEvent(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    destination = models.CharField(max_length=122)
    date = models.DateField(null=True)
    time = models.TimeField(null=True)
    desc = models.TextField(max_length=500,null=True)
    guest = models.CharField(max_length=500,null=True)
    

    def __str__(self):
        return self.name
    

class PartiesEvent(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    destination = models.CharField(max_length=122)
    date = models.DateField(null=True)
    time = models.TimeField(null=True)
    desc = models.TextField(max_length=500,null=True)
    guest = models.CharField(max_length=500,null=True)
    

    def __str__(self):
        return self.name
    

class WeddingEvent(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    destination = models.CharField(max_length=122)
    date = models.DateField(null=True)
    time = models.TimeField(null=True)
    desc = models.TextField(max_length=500,null=True)
    guest = models.CharField(max_length=500,null=True)
    

    def __str__(self):
        return self.name
    
class TechnicalEvent(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    destination = models.CharField(max_length=122)
    date = models.DateField(null=True)
    time = models.TimeField(null=True)
    desc = models.TextField(max_length=500,null=True)
    guest = models.CharField(max_length=500,null=True)
    

    def __str__(self):
        return self.name
