from django.test import TestCase
from rest_framework.permissions import IsAuthenticated

# Create your tests here.

from rest_framework.test import APITestCase

from online_learning.models import Lesson, Course, Subscription
from users.models import User

from django.urls import reverse
from rest_framework import status, serializers

from users.permissions import IsOwnerClass, IsModeratorClass


class LessonTestCase(APITestCase):

    def setUp(self):
        # Подготовка данных перед каждым тестом
        self.user = User.objects.create(
            email='test_user@test_user.ru',
            first_name='test_user',
            last_name='test_user',
            is_staff=False,
            is_superuser=False
        )
        self.course = Course.objects.create(
            title='test_course',
            description='test_course',
            owner=self.user
        )
        self.lesson = Lesson.objects.create(
            title='test_lesson_1',
            description='test_lesson_1',
            course=self.course,
            owner=self.user
        )
        self.client.force_authenticate(user=self.user)

    def test_lesson_retrieve(self):
        url = reverse('online_learning:lesson', args=(self.lesson.pk,))
        response = self.client.get(url)
        data = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get('title'), self.lesson.title)

    def test_lesson_create(self):
        new_text = 'test_lesson_2'
        url = reverse('online_learning:lesson_create')
        data = {
            'title': new_text,
            'description': new_text,
            'course': self.course.pk
        }
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Lesson.objects.all().count(), 2)
        self.assertEqual(Lesson.objects.get(title=new_text).owner, self.user)

    def test_lesson_update(self):
        new_text = 'test_lesson_updated'
        url = reverse('online_learning:lesson_update', args=(self.lesson.pk,))
        data = {'title': new_text}
        response = self.client.patch(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('title'), new_text)

        new_url = 'YOUtube.com/12345'
        data = {'url': new_url}
        response = self.client.patch(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('url'), new_url)

        new_url = ''
        data = {'url': new_url}
        response = self.client.patch(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('url'), new_url)

        new_url = 'hello.com/12345'
        data = {'url': new_url}
        response = self.client.patch(url, data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_lesson_delete(self):

        url = reverse('online_learning:lesson_delete', args=(self.lesson.pk,))

        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Lesson.objects.all().count(), 1)

        #self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        #self.assertEqual(Lesson.objects.all().count(), 0)

    def test_lesson_list(self):
        url = reverse('online_learning:lessons_list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data,
            {
                'count': 1,
                'next': None,
                'previous': None,
                'results':
                    [
                        {
                            'id': self.lesson.pk,
                            'title': self.lesson.title,
                            'description': self.lesson.description,
                            'picture': None,
                            'url': None,
                            'course': self.lesson.course.pk,
                            'owner': self.lesson.owner.pk
                        }
                    ]
            }
        )


class SubscriptionTestCase(APITestCase):

    def setUp(self):
        # Подготовка данных перед каждым тестом
        self.user = User.objects.create(
            email='test_user@test_user.ru',
            first_name='test_user',
            last_name='test_user',
            is_staff=False,
            is_superuser=False
        )
        self.course = Course.objects.create(
            title='test_course',
            description='test_course',
            owner=self.user
        )
        self.lesson = Lesson.objects.create(
            title='test_lesson_1',
            description='test_lesson_1',
            course=self.course,
            owner=self.user
        )
        self.subscription = Subscription.objects.create(
            course=self.course,
            user=self.user
        )
        self.client.force_authenticate(user=self.user)

    def test_subscription(self):
        url = reverse("online_learning:subscription")
        data = {
            "course": self.course.pk
        }
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('message'), 'Подписка отключена')

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('message'), 'Подписка включена')
