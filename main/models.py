from django.db import models
from django.contrib.auth.models import User

class Cauntry(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=255)
    cauntry = models.ForeignKey(Cauntry, related_name="cauntry", on_delete=models.CASCADE)

    def __str__(self): 
        return self.name


class Masque(models.Model):
    admin = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=255)
    city = models.ForeignKey(City, related_name="city", on_delete=models.CASCADE)
    capacity = models.PositiveIntegerField()
    bio = models.TextField()

    def __str__(self):
        return f"{self.name} {self.city.name}"


class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    CHOICE = {
        (1,'Imom'),
        (2,'Imom hatib'),
        (3,'Qori'),
        (4,'Muazzin')
    }
    f_name = models.CharField( max_length=250)
    l_name = models.CharField( max_length=250)
    staff = models.IntegerField(choices=CHOICE)
    bio = models.TextField()
    image = models.ImageField(upload_to="hodim/")
    masque = models.ForeignKey(Masque, related_name='masque', on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.f_name} {self.masque.name}"


class ImageMasque(models.Model):
    masqueimg = models.ForeignKey(Masque, related_name='masque_photo', on_delete=models.CASCADE )
    image = models.ImageField(upload_to="masque/")

    def __str__(self):
        return self.masqueimg.name
    

class PrayerTime(models.Model):
    frm = models.DateField()
    morning = models.TimeField()
    Afternoon = models.TimeField()
    Evening = models.TimeField()
    Night = models.TimeField()
    Midnight = models.TimeField()
    to = models.DateField()
    masquet = models.OneToOneField(Masque, related_name='masque_time', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.masquet.name} {self.masquet.city.name}"
    