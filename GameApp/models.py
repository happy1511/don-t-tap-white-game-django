from django.db import models

# Create your models here.
class Score(models.Model):

    username = models.CharField(max_length=100)
    highestscore = models.CharField(max_length=100)
    history = models.JSONField()

    def __str__(self):
        return self.username