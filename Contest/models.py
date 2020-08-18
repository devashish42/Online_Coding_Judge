from django.db import models
from Problem.models import problem
from django.contrib.auth.models import User

class contest(models.Model):
    name = models.CharField(max_length=100,unique=True,default='contest')
    description = models.TextField()
    problems = models.ManyToManyField(problem)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    participants = models.ManyToManyField(User,through='leaderBoard')
    def __str__(self):
        return self.name

class leaderboard(models.Model):
    name = models.CharField(max_length=70,null=True)
    user = models.ForeignKey(User,null=True,on_delete=models.CASCADE)
    contest_board = models.ForeignKey(contest,null=True,on_delete=models.CASCADE)
    score = models.IntegerField(null=True,blank=True)

    class Meta:
        unique_together=[['user','contest_board']]

    def __str__(self):
        return self.name