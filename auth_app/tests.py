from django.test import TestCase
from django.contrib.auth import get_user_model

User = get_user_model()

class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create_user(
            username="testuser",
            email="testuser@example.com",
            phone_number="1234567890",
            password="securepassword123"
        )
        self.assertEqual(user.username, "testuser")
        self.assertFalse(user.is_verified)

    def test_create_superuser(self):
        admin = User.objects.create_superuser(
            username="admin",
            email="admin@example.com",
            phone_number="0987654321",
            password="securepassword123"
        )
        self.assertTrue(admin.is_superuser)
