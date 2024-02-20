from django.db import models

# Create your models here.

class IpModel(models.Model):
    ip = models.CharField(max_length=100)

    def __str__(self):
        return self.ip
    
class PageViews(models.Model):
    views = models.ManyToManyField(IpModel, related_name="post_views", blank=True)

    def __str__(self):
        return self.views