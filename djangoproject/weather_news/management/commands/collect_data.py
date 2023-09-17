import requests
import logging
from django.core.management.base import BaseCommand
from models import Weather, News

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'Collects data from external APIs and stores it in the database.'

    def handle(self, *args, **options):
        openweather_api_key = "d5b542afd54010f86dd99dad0d597f21"
        news_api_key = "52e7ec5b90cf4cdbb8d9c029286912e0"

        # Fetch weather data from OpenWeather API
        cities = ['London', 'Berlin', 'Oslo', 'Paris', 'Rome', 'New York']

        for city in cities:
            payload = {'q': city, 'appid': openweather_api_key}
            response = requests.get('http://api.openweathermap.org/data/2.5/weather/', params=payload).json()

            if response.get('cod') == 200:
                temperature = response.get('main').get('temp')
                weather = response.get('weather')[0].get('main')
                temperature = temperature - 273.15

                Weather.objects.create(
                    city=city,
                    temperature=temperature,
                    weather=weather
                )
                logger.info('Saved weather for %s: %s°C - %s', city, temperature, weather)
                print(f'Saved weather for {city}: {temperature}°C - {weather}')
            else:
                logger.warning('Failed to fetch weather data for %s.', city)
                print(f'Failed to fetch weather data for {city}.')

        # Fetch news data from NewsAPI
        url = f'https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey={news_api_key}'
        response = requests.get(url).json()

        if response.get('status') == 'ok':
            articles = response.get('articles')
            for article in articles:
                title = article.get('title')
                description = article.get('description')
                source = article.get('source').get('name')
                author = article.get('author')

                News.objects.create(
                    title=title,
                    description=description,
                    source=source,
                    author=author
                )
                logger.info('Saved news article: %s', title)
                print(f'Saved news article: {title}')
        else:
            logger.error('Failed to fetch news data from NewsAPI.')
            print('Failed to fetch news data from NewsAPI.')
