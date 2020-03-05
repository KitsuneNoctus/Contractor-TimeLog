from django import forms
from TimeLog.models import Class


class ClassForm(forms.ModelForm):
    """ Render and process a form based on the Page model. """
    class Meta:
        model = Class
        fields = ['class_name','class_description','class_start_date','class_end_date']