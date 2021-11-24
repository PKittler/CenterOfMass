from django.db import models
from math import sqrt, pow, sin, cos, acos, tan, atan, atan2, degrees, radians, fabs

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
    x_value = models.FloatField(default=0)
    y_value = models.FloatField(default=0)
    z_value = models.FloatField(default=0)
    mass = models.FloatField(default=1)

    def __str__(self):
        return self.lastname

    def calculate_radius3D(self):
        return sqrt(pow(self.x_value,2) + pow(self.y_value,2) + pow(self.z_value,2))

    def calculate_radius2D(self):
        return sqrt(pow(self.x_value,2) + pow(self.y_value,2))

    radius_3D = property(calculate_radius3D)
    radius_2D = property(calculate_radius2D)

    def deg_theta(self):
        try:
            pre_value = self.z_value / self.radius_3D
        except ZeroDivisionError:
            pre_value = 0

        try:
            value = degrees(acos(pre_value))
        except:
            value = 0

        print("Theta:", pre_value, "|", value, "°")
        return value


    def deg_phi(self):
        try:
            pre_value = self.x_value / self.radius_2D
        except ZeroDivisionError:
            pre_value = 0

        try:
            value = degrees(acos(pre_value))
        except:
            value = 0

        print("Phi:", pre_value, "|", value, "°")
        return value

    theta = property(deg_theta)
    phi = property(deg_phi)

    def calculate_x(self):
        print("\n")
        print("-----------------------------------------------------------")
        print("========= CALCULATE X =========")
        print("P(", self.x_value, "|", self.y_value, "|", self.z_value, ")")

        value = fabs(self.x_value) * sin(radians(self.theta)) * cos(radians(self.phi))

        print("Result X:", value, "\n")

        return value

    def calculate_y(self):
        print("========= CALCULATE Y =========")
        print("P(", self.x_value, "|", self.y_value, "|", self.z_value, ")")
        value = self.y_value * sin(radians(self.theta)) * sin(radians(self.phi))

        print("Result Y:", value, "\n")

        return value

    def calculate_z(self):
        print("========= CALCULATE Z =========")
        print("P(", self.x_value, "|", self.y_value, "|", self.z_value, ")")

        value = fabs(self.z_value) * cos(radians(self.theta))

        print("Result Z:", value, "\n")

        return value

    x_calc = property(calculate_x)
    y_calc = property(calculate_y)
    z_calc = property(calculate_z)


class CSV_masspoints_file(models.Model):
    case = models.ForeignKey(Case, on_delete=models.CASCADE)
    upload_file = models.FileField(null=True, blank=True,upload_to='media')
    upload_date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.case.id