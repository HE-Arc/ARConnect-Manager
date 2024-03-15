from django.db import models
from django.contrib.auth.models import User

#Tournament model
class TournamentItem(models.Model):
    name = models.CharField(max_length=100)             #Name of the tournament
    description = models.TextField()                    #Description of the tournament
    state = models.IntegerField()                       #State of the tournament : 0=open, 1=started, 2=finished
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)