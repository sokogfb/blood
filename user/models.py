from django.db import models


class Info(models.Model):
    CHOICES = (('A+', 'A+'),
               ('B+', 'B+'),
               ('A-', 'A-'),
               ('B-', 'B-'),
               ('AB+', 'AB+'),
               ('AB-', 'AB-'),
               ('O+', 'O+'),
               ('O-', 'O-'))
    name = models.CharField(max_length=50)
    age = models.PositiveSmallIntegerField(blank=True, null=True)
    email = models.EmailField(max_length=50)
    address = models.CharField(max_length=50)
    contact_number = models.CharField(max_length=30)
    blood_group = models.CharField(max_length=5, choices=CHOICES)

    def __str__(self):
      return "Name: {}, Age: {}, Blood group: {}".format(self.name, self.age, self.blood_group)






