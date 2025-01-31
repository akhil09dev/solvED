from django.db import models

# Syllabus

class Board(models.Model):
    name= models.CharField(max_length=100,unique=False)
    def __str__(self):
        return self.name

class Grade(models.Model):
    name= models.CharField(max_length=100,unique=True)
    board=models.ForeignKey(Board,on_delete=models.SET_NULL,null=True, related_name='streams')
    def __str__(self):
        return self.name

class Subject(models.Model):
    name= models.CharField(max_length=100,unique=False)
    grade=models.ForeignKey(Grade,on_delete=models.SET_NULL,null=True, related_name='subject')
    def __str__(self):
        return self.name

class Chapter(models.Model): 
    name=models.CharField(max_length=100,unique=False)
    subject= models.ForeignKey(Subject,on_delete=models.SET_NULL,null=True,related_name='chapters')
    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.name


# content
class Solution(models.Model):
    content= models.TextField()
    figure=models.URLField(null=True,blank=True)

class Question(models.Model):
    content= models.TextField()
    figure = models.URLField(blank=True, null=True)
    options= models.JSONField(default=list)
    correct_option=models.PositiveIntegerField()
    solution= models.ForeignKey(Solution,on_delete=models.SET_NULL, null=True, related_name='questions' )
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="questions")
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, related_name='questions')


