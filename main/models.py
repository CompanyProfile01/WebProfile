from django.db import models

# Create your models here.


class Visitor(models.Model):
    ip = models.CharField(max_length=100)
    lastVisit = models.DateTimeField()

    def __str__(self):
        return self.ip
    
class PageViews(models.Model):
    views =  models.IntegerField()

    def __str__(self):
        return self.views