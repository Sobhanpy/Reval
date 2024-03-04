from django.db import models

class Service(models.Model):
    title = models.CharField(max_length = 255)
    content = models.CharField(max_length = 600)
    status = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title