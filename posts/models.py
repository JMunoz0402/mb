from django.db import models


class Post(models.Model):                                    #inheritance
    title = models.CharField(max_length=128)                #compostion
    subtitle = models.CharField(max_length=256)             #compostion
    body = models.TextField()                               #compostion
    created_on = models.DateTimeField(auto_now_add=True)    #compostion

def __str__(self):
    return self.title