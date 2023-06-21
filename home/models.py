from django.db import models

# Create your models here.
class Our_Media(models.Model):
    title = models.CharField(max_length=30)
    image = models.ImageField(blank=True,upload_to='images/')

    
    def __str__(self):
        return self.title