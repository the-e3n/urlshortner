from django.db import models
import nanoid
# Create your models here.




class Urls(models.Model):
    slug = models.CharField(max_length=8,unique=True)
    url = models.URLField(unique=True)
    views = models.IntegerField(default=0)


    def __str__(self):
        return self.url
