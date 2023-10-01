from django.db import models

# Create your models here.
class Tile(models.Model):

    TileNo = models.CharField(max_length=1,default=0)
    TileColor = models.CharField(max_length=5)