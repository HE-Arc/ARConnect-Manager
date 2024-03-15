from django.db import models

# Create your models here.
class TournamentItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    state = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)