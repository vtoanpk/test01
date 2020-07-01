from django.test import TestCase
from django.contrib.auth import get_user_model


class UsersManagersTests(TestCase):


    def test_create_user(self):
        User =get_user_model()
        user = User.objects.create_user(
            email='normal@user.com',
            password='normal1234',
            first_name='first',
            last_name='last',
            )
        self.assertEqual(user.email, 'normal@user.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        try:
            self.assertIsNone(user.username)
        except AttributeError:
            pass
        with self.assertRaises(TypeError):
            User.objects.create_user()
        with self.assertRaises(TypeError):
            User.object.create_user(email='')
        with self.assertRaises(ValueError):
            User.objects.create_user(email='', password='normal1234')


    def test_create_superuser(self):
        User = get_user_model()
        admin_user = create_superuser('super@user.com', 'super1234')
        self.assertEqual(admin_user.email, 'super@user.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
        try:
            self.assertIsNone(admin_user.username)
        except AttributeError:
            pass
        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                email='super@user.com',
                password='super1234',
                is_superuser=False
            )