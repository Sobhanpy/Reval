from django.db import models

class Testimonial(models.Model):
    name = models.CharField(max_length = 255)
    family = models.CharField(max_length = 255)
    job = models.CharField(max_length = 255)
    image = models.ImageField (upload_to = '/media/team/')
    description = models.CharField(max_length = 700)

    def __str__(self):
        return self.name