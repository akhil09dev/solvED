from django.db import models


# content
class Solution(models.Model):
    content= models.TextField()
    figure=models.URLField(null=True,blank=True)

class Questions(models.Model):
    content= models.TextField()
    figure = models.URLField(blank=True, null=True)
    options= models.JSONField(default=list)
    correct_option=models.PositiveIntegerField()
    solution= models.ForeignKey(Solution,on_delete=models.SET_NULL, null=True, related_name='questions' )

# Syllabus
class Grade(models.Model):
    name= models.CharField(max_length=100,unique=True)
    
class Stream(models.Model):
    name= models.CharField(max_length=100,unique=False)
    grade=models.ForeignKey(Grade,on_delete=models.SET_NULL,null=True, related_name='streams')

class Subject(models.Model):
    name= models.CharField(max_length=100,unique=False)
    grade=models.ForeignKey(Grade,on_delete=models.SET_NULL,null=True, related_name='subject')
    stream=models.ForeignKey(Stream,on_delete=models.SET_NULL,null=True, related_name='subjects')

class Chapter(models.Model): 
    name=models.CharField(max_length=100,unique=False)
    subject= models.ForeignKey(Subject,on_delete=models.SET_NULL,null=True,related_name='chapters')
