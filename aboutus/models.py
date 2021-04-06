from django.db import models

# Create your models here.
class CarouselHome(models.Model):
    title = models.CharField(max_length=200)
    cover = models.ImageField(upload_to='carousel_home/', blank=True)

    def __str__(self):
        return self.title

class NewsHome(models.Model):
    title = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='news_home/', blank=True)
    content = models.TextField(max_length=500)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.title