from django.db import models



# Create your models here.
class Post(models.Model):
 name = models.CharField(max_length=255)
 catagry = models.SlugField()
 price = models.TextField()
 image = models.TextField()
 rate = models.TextField()
 date_added = models.DateTimeField(auto_now_add=True)

 class Meta:
  ordering = ['-date_added']
