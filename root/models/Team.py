from django.db import models

class Team(models.Model):
    name = models.CharField(max_length = 255)
    family = models.CharField(max_length = 255)
    job = models.CharField(max_length = 255)
    image = models.ImageField (upload_to = '/media/team/')
    instagram = models.CharField(defult = "https://www.instagram.com/Sobhan.py")
    twitter = models.CharField(defult = "https://www.instagram.com/Sobhan.py")
    linkdin = models.CharField(defult = "https://www.linkdin.com/Sobhan.py")
    facebook = models.CharField(defult = "https://www.instagram.com/Sobhan.py")

    def __str__(self):
        return self.name