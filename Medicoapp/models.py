from django.db import models

# Create your models here.
class product(models.Model) :
    name = models.CharField(max_length=200)
    quantity = models.IntegerField()
    price = models.CharField(max_length=200)
    colour = models.CharField(max_length=20)
    description = models.TextField()
    def __str__(self):
        return self.name


class branch(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    manager = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    message = models.TextField()
    def __str__(self):
        return self.name

class appointment(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    department = models.CharField(max_length=200)
    date = models.DateField()
    doctor = models.CharField(max_length=200)
    message = models.TextField()
    def __str__(self):
        return self.name

class members(models.Model):
    name = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class ImageModel(models.Model):
        image = models.ImageField(upload_to='images/')
        title = models.CharField(max_length=50)
        price = models.CharField(max_length=50)
        def __str__(self):
            return self.title

class Admin(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    def __str__(self):
        return self.username