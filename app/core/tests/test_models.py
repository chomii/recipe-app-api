from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test create user with email is successful"""
        email = "test@gmail.com"
        password = "test12345"
        user = get_user_model().objects.create_user(
            email=email, password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email for the new user is normalized."""
        email = 'test@GMAIL.COM'
        user = get_user_model().objects.create_user(email, 'test12345')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises errir """

        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test12345')

    def test_create_new_superuser(self):
        """Test creating new superuser """

        user = get_user_model().objects.create_superuser('test@gmail.com', 'test12345')

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
