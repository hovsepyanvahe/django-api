from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):

    def test_create_user_with_email_successfull(self):
        email = 'test@test.com'
        password = 'changeme123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))


    def test_new_user_email_mormalized(self):
        email = 'test@LMSKSMKSM.COM'
        user = get_user_model().objects.create_user(email, 'changeme123')

        self.assertEqual(user.email, email.lower())
