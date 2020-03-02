import datetime
from django.utils import timezone
from django.db import models

# Create your models here.
class Class(models.Model):
    ''' To create a full class '''
    class_name = models.CharField(max_length=50)
    class_description = models.CharField(max_length=200)
    class_start_date = models.DateTimeField('Start Date')
    class_end_date = models.DateTimeField('End Date')
    def __str__(self):
        return self.class_description

# def Home()