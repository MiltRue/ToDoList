from django.test import TestCase

# Create your tests here.
class PracticeTest(TestCase):
    def test_failure(self):
        self.assertEqual(1+1,3)