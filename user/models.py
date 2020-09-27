from django.db import models


class Facility(models.Model):
    PROVINCES = (
        ('Central', 'Central'),
        ('Copperbelt', 'Copperbelt'),
        ('Eastern', 'Eastern'),
        ('Lusaka', 'Lusaka'),
        ('Luapula', 'Luapula'),
        ('Muchinga', 'Muchinga'),
        ('Southern', 'Southern'),
        ('Western', 'Western'),
        ('Northen', 'Northen'),
        ('North-Wetern', 'North-Western')

    )
    FACILITY_CAT = (
        ('Level 1', 'Level 1'),
        ('Level 2', 'Level 2'),
        ('Level 3', 'Level 3'),
        ('Rural Facility', 'Rural Facility'),
        ('Urban Facility', 'Urban Facility'),
    )
    facility_id = models.CharField(max_length=20)
    province = models.CharField(max_length=25, choices=PROVINCES)
    category = models.CharField(max_length=25, choices=FACILITY_CAT)

    def __str__(self):
        return "Facility: {}, Province: {}, Category: {}".format(self.facility_id, self.province, self.category)


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
