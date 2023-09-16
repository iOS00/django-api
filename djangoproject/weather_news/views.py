from django.shortcuts import render
from rest_framework import generics
from .models import Weather, News
from .serializers import WeatherSerializer, NewsSerializer
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiTypes
import logging

logger = logging.getLogger(__name__)

@extend_schema(
    description='Retrieve weather data.',
    parameters=[
        OpenApiParameter(
            name='city',
            description='Filter weather data by city',
            required=False,
            type=OpenApiTypes.STR,
            location=OpenApiParameter.QUERY
        ),
        OpenApiParameter(
            name='temperature__gte',
            description='Filter weather data by minimum temperature',
            required=False,
            type=OpenApiTypes.NUMBER,
            location=OpenApiParameter.QUERY
        )
    ],
    responses={200: WeatherSerializer}
)
class WeatherListAPIView(generics.ListAPIView):
    queryset = Weather.objects.all()
    serializer_class = WeatherSerializer

    def get_queryset(self):
        queryset = super().get_queryset()

        # filter the queryset based on parameters
        city = self.request.query_params.get('city')
        temperature__gte = self.request.query_params.get('temperature__gte')  # greater than
        if city:
            queryset = queryset.filter(city=city)
        if temperature__gte:
            queryset = queryset.filter(temperature__gte=temperature__gte)
        if city and temperature__gte:
            queryset = queryset.filter(city=city, temperature__gte=temperature__gte)
        return queryset

    def get(self, request, *args, **kwargs):
        # Perform any additional logic
        logger.debug('Get request received for the WeatherListAPIView')
        return super().get(request, *args, **kwargs)



@extend_schema(
    description='Retrieve news data.',
    parameters=[
        OpenApiParameter(
            name='source',
            description='Filter news data by source',
            required=False,
            type=OpenApiTypes.STR,
            location=OpenApiParameter.QUERY
        ),
        OpenApiParameter(
            name='author',
            description='Filter news data by author',
            required=False,
            type=OpenApiTypes.STR,
            location=OpenApiParameter.QUERY
        )
    ],
    responses={200: WeatherSerializer}
)
class NewsListAPIView(generics.ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

    def get_queryset(self):
        queryset = super().get_queryset()

    # filter queryset with raw sql queries
        source = self.request.query_params.get('source')
        author = self.request.query_params.get('author')

        if source:
            queryset = News.objects.raw("SELECT * FROM weather_news_news WHERE source = %s", [source])
        if author:
            queryset = News.objects.raw("SELECT * FROM weather_news_news WHERE author = %s", [author])
        if source and author:
            queryset = News.objects.raw(
                """
                SELECT * FROM weather_news_news WHERE source =%s
                AND author = %s""", [source, author])
        return queryset

    def get(self, request, *args, **kwargs):
        # Perform any additional logic
        logger.debug('GET request received for NewsListAPIView')
        return super().get(request, *args, **kwargs)
