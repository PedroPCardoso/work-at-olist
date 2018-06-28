from django.test import TestCase

from core.models import CallInitial,CallEnd
from rest_framework.test import APIRequestFactory, APIClient

from rest_framework import status
from django.urls import reverse
from django.test import TestCase, Client
import json

class ModelTestCase(TestCase):
    def test_model_can_create_a_callinitial(self):
        """Test the call initial model can create a callinitial."""
        self.callini = CallInitial(destination="99999999", source="88888888", call_id=23,
                                   time="2011-07-14T19:43:37+0100")
        old_count = CallInitial.objects.count()
        self.callini.save()
        new_count = CallInitial.objects.count()
        self.assertNotEqual(old_count, new_count)
    def test_model_can_create_a_callEnd(self):
        """Test the call initial model can create a callinitial."""
        self.callini = CallEnd(call_id=23,time="2011-07-14T19:43:37+0100")
        old_count = CallEnd.objects.count()
        self.callini.save()
        new_count = CallEnd.objects.count()
        self.assertNotEqual(old_count, new_count)



class ViewTestCase(TestCase):
    """Test suite for the api views."""
    def test_api_can_create_a_calls(self):
        """Define the test client and other test variables."""
        self.client = APIClient()
        self.callinitial_data = {
            'destination' : "99999999", 'source' : "88888888", 'call_id' : 13, 'time' : "2011-07-14T19:43:37+0100"
        }
        self.response = self.client.post('/calls/',
            self.callinitial_data,
            format="json")
        """Test the api has calls creation capability."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
