from django.test import TestCase
from django.contrib.auth.models import User
from TimeLog.models import Class
from django.utils import timezone
import datetime

class TimeLogTestCase(TestCase):
    def test_true_is_true(self):
        """ Tests if True is equal to True. Should always pass. """
        self.assertEqual(True, True)

    def test_class_slugify_on_slave(self):
        """Test slug generated for Class"""

        # Create and save new class
        clas = Class(class_name="Test Page", class_description="Test description", class_start_date=datetime.date(2020,12,30),class_end_date=datetime.date(2020,12,31))
        clas.save()

        #Assert
        self.assertEqual(clas.slug, "test-page")
        self.assertEqual(clas.get_absolute_url(), "/test-page/")
