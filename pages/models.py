from django.db import models

# Create your models here.
class Pokenea(models.Model):
  name = models.CharField(max_length=255)
  height = models.IntegerField()
  skill = models.CharField(max_length=255)
  image = models.CharField(max_length=255)
  phrase = models.CharField(max_length=255)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.name