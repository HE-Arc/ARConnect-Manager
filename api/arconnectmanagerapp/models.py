from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

#Tournament model
class TournamentItem(models.Model):
    name = models.CharField(max_length=100)             #Name of the tournament
    description = models.TextField()                    #Description of the tournament
    state = models.IntegerField(                        #State of the tournament : 0=closed, 1=open, 2=started 3=finished
            default=0,
            validators=[MinValueValidator(0), MaxValueValidator(3)]
        )                       
    players = models.ManyToManyField(User, related_name='players')
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)