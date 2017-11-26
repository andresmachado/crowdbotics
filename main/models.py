from django.db import models

# Create your models here.


class Animal(models.Model):
    owner = models.ForeignKey('auth.User')
    name = models.CharField(max_length=50)
    birthday = models.DateField()

    class Meta:
        abstract = True


class Dog(Animal):
    def __str__(self):
        return self.name


class Cat(Animal):
    def __str__(self):
        return self.name

