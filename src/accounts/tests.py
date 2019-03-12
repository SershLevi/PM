from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


class SignUpPageTests(TestCase):
    email = 'newuser@email.com'

    def test_signup_page_status_code(self):
        response = self.client.get('/accounts/signup/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/signup.html')

    def test_signup_form(self):
        get_user_model().objects.create_user(self.email)
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].email, self.email)


# @override_settings(
#     DISABLE_GENERIC_PERMISSION_CACHE=True
# )
# class AutoMemberTest(TestCase):
#
#     def setUp(self):
#         self.test_user = Account.objects.create(
#             email='test@test.com'
#         )
#         self.test_user2 = Account.objects.create(
#             email='test2@test.com'
#         )
#         self.test_user3 = Account.objects.create(
#             email='test3@test.com'
#         )
#         self.post = Project.objects.create(
#             author=self.test_user
#         )
#         self.manage_post_perm = Permission.objects.get(
#             content_type__app_label='test_app',
#             codename='manage_post'
#         )
#         GenericGlobalPerm.objects.create(
#             permission=self.manage_post_perm,
#             roles=Project.PROJECT_MANAGER,
#             content_type=ContentType.objects.get_for_model(Project)
#         )
#
#     def test_auto_member_on_create(self):
#         self.assertTrue(
#             self.test_user.has_perm('test_app.manage_post', self.post)
#         )
#
#     def test_auto_member_on_update(self):
#         self.assertFalse(
#             self.test_user2.has_perm('test_app.manage_post', self.post)
#         )
#         Project.objects.filter(id=self.post.id).update(author=self.test_user2)
#         self.assertTrue(
#             self.test_user2.has_perm('test_app.manage_post', self.post)
#         )
#
#     def test_auto_member_on_save(self):
#         self.assertFalse(
#             self.test_user3.has_perm('test_app.manage_post', self.post)
#         )
#         self.post.author = self.test_user3
#         self.post.save()
#         self.assertTrue(
#             self.test_user3.has_perm('test_app.manage_post', self.post)
#         )
