from django.urls import path
from .views import WeatherListAPIView, NewsListAPIView

app_name = 'weather_news'

urlpatterns = [
    path('weather/', WeatherListAPIView.as_view(), name='weather-list'),
    path('news/', NewsListAPIView.as_view(), name='news-list'),
]
