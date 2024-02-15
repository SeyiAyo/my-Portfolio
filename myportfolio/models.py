from django.db import models


class about(models.Model):
    short_intro = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/', null = True, blank=True)
    description = models.TextField()

    def __str__(self):
        return "About ME"
    
    
class project(models.Model):
    title = models.CharField(max_length=100)
    #slug = models.SlugField()
    image = models.ImageField(upload_to='images/')
    url = models.URLField()

    def __str__(self):
        return self.title
    
    
    
class contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name