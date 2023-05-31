from django.db import models


class ClwbAdmin(models.Model):
   
    month = models.CharField(max_length=254)
    name = models.CharField(max_length=254)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return self.name
