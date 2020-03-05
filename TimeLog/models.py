import datetime
from django.utils import timezone
from django.db import models

# Create your models here.
class Class(models.Model):
    ''' To create a full class '''
    class_name = models.CharField(max_length=50, help_text="Class Name")
    class_description = models.TextField(help_text="Enter Class Description Here.")
    class_start_date = models.DateTimeField('Start Date')
    class_end_date = models.DateTimeField('End Date')
    modified = models.DateTimeField(auto_now=True,
                                    help_text="The date and time this page was updated. Automatically generated when the model updates.")
    def __str__(self):
        return self.class_description

# def Home()