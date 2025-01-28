from django.test import TestCase
from django.contrib.auth.models import User

from profiles.models import Profile


class ProfileModelTest(TestCase):
    databases = {'test'}

    def setUp(self):
        User.objects.all().delete()
        Profile.objects.all().delete()

        self.user = User.objects.create_user(username='testuser', password='testpassword')

        self.profile = Profile.objects.create(
            user=self.user,
            birth_date='2025-01-28',
            tg_username='test_user',
        )

    def test_profile_creation(self):
        self.assertEqual(self.profile.user.username, 'testuser')
        self.assertEqual(self.profile.birth_date, '2025-01-28')
        self.assertEqual(self.profile.tg_username, 'test_user')

    def test_default_avatar(self):
        profile_with_default_avatar, _ = Profile.objects.get_or_create(user=self.user)
        self.assertEqual(profile_with_default_avatar.avatar, 'avatars/no_avatar.png')

    def test_user_relationship(self):
        self.assertEqual(self.profile.user, self.user)
        self.assertTrue(hasattr(self.user, 'profile'))
