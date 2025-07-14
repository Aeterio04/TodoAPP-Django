from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
class TodoTask(models.Model):
    
    taskUser=models.ForeignKey(User, on_delete=models.CASCADE)
    taskTitle=models.CharField(max_length=200, null=False, blank= False)
    taskDesc=models.CharField(max_length=500, null=False, blank= False)
    taksTime=models.DateTimeField(default=datetime.now)
    taskStat=models.BooleanField(default=0)     

# Create your models here.
