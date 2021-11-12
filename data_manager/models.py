from django.db import models

class Case(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    label_x_min = models.CharField(max_length=30)
    label_x_max = models.CharField(max_length=30)
    label_y_min = models.CharField(max_length=30)
    label_y_max = models.CharField(max_length=30)
    label_z_min = models.CharField(max_length=30)
    label_z_max = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Masspoint(models.Model):
    case = models.ForeignKey(Case, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    x_value = models.IntegerField(default=0)
    y_value = models.IntegerField(default=0)
    z_value = models.IntegerField(default=0)
    mass = models.FloatField(default=0)

    def __str__(self):
        return self.lastname