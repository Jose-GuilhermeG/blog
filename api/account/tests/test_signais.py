#imports
from django.test import TestCase
from model_bakery import baker

#models
from account.models import Profile
from django.contrib.auth import get_user_model

USER = get_user_model()


class UserSignalsTestCase(TestCase):
    def test_if_profile_is_created_on_user_creation(self):
        user = baker.make(USER)
        profile = Profile.objects.filter(user=user).first()
        self.assertIsNotNone(profile)
        self.assertEqual(profile.user,user)