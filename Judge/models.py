from django.db import models
from django.contrib.auth.models import User
from Problem.models import testCase, problem

class programmingLanguage(models.Model):

    # Class Variables
    languageChoices = (('P','Python'),('C','C++'),('J','Java'),('c','C'))
    
    # Model Variables
    name = models.CharField(max_length=1,choices=languageChoices)

    def __str__(self):
        return self.name


class verdict(models.Model):

    # Class Variables
    verdictChoices=(('A','Accepted'),('WA','Wrong Answer'),('C','Compilation Error'),('S','Segmentation Fault'),)
    
    # Model Variables
    status_code=models.CharField(max_length=2,choices=verdictChoices)
    message= models.CharField(max_length=100)

    def __str__(self):
        return self.status_code

class submission(models.Model):
    unique_slug = models.SlugField(unique = True)
    verdict = models.OneToOneField(verdict,on_delete=models.CASCADE)
    programming_language = models.OneToOneField(programmingLanguage,on_delete=models.CASCADE)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    problems = models.OneToOneField(problem,on_delete=models.SET_NULL,blank=True,null=True)
    code = models.TextField(max_length=10000)
    
    def __str__(self):
        return self.id

class submissionDetails(models.Model):

    # Class Variables 
    isCorrectChoices = (('P','Passed'),('F','Failed'),)
    
    # Model Variables
    submission_details=models.OneToOneField(submission,on_delete=models.CASCADE)
    testcase_id=models.OneToOneField(testCase,on_delete=models.CASCADE)
    is_correct=models.CharField(max_length=1,choices=isCorrectChoices)
    
    def __str__(self):
        return self.is_correct