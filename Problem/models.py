from django.db import models
from django.contrib.auth.models import User

class testCase(models.Model):
    problem_input = models.CharField(max_length=100)
    correct_output=models.CharField(max_length=100)

    def __str__(self):
        return self.id

class problem(models.Model):

    # Class Variables
    levelChoices = (('E','Easy'),('M','Medium'),('H','Hard'),)
    
    # Model Variables
    name = models.CharField(max_length=100,unique=True)
    author = models.ForeignKey(User,on_delete = models.SET_NULL, blank=True, null=True)
    problem_statement = models.TextField()
    input_format = models.TextField()
    output_format = models.TextField()
    time_limit = models.IntegerField()
    memory_limit = models.IntegerField()
    test_cases = models.ManyToManyField(testCase)
    problem_level = models.CharField(max_length=1,choices=levelChoices)
    maximum_marks = models.IntegerField()
    
    def __str__(self):
        return self.name