from django.test import TestCase
from django.urls import reverse
from management.commands.collect_data import Command
from .models import Weather, News
from rest_framework.test import APIClient


class WeatherModelTestCase(TestCase):

    def test_save_weather(self):
        weather = Weather.objects.create(city='London', temperature=20.5, weather='Cloudy')
        self.assertEqual(Weather.objects.count(), 1)


class NewsModelTestCase(TestCase):
    def test_save_news(self):
        news = News.objects.create(
            title='Test News',
            description='This is a test news article',
            source='Test Source',
            author='John Doe'  # Provide a valid author value
        )
        self.assertEqual(News.objects.count(), 1)


class WeatherListAPIViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_weather_list_api_view(self):
        response = self.client.get(reverse('weather_news:weather-list'))
        self.assertEqual(response.status_code, 200)


class NewsListAPIViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_news_list_api_view(self):
        response = self.client.get(reverse('weather_news:news-list'))
        self.assertEqual(response.status_code, 200)


class CollectDataCommandTestCase(TestCase):
    def test_collect_data_command(self):
        command = Command()
        command.handle()
        self.assertEqual(Weather.objects.count(), 6) #number of cities
        self.assertGreater(News.objects.count(), 0)
