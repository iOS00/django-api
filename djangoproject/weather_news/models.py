from django.db import models
import logging

logger = logging.getLogger(__name__)


class Weather(models.Model):
    city = models.CharField(max_length=100)
    country = models.CharField(max_length= 100)
    weather = models.CharField(max_length=100)
    temperature = models.FloatField()

    class Meta:
        unique_together = ('city', 'weather')

    def save(self, *args, **kwargs):
        # Perform any additional logic before saving the instance
        logger.info('Saving weather instance: %s', self)
        super().save(*args, **kwargs)


class News(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    source = models.CharField(max_length=100)
    author = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        unique_together = ('title', 'source')

    def save(self, *args, **kwargs):
        # Perform any additional logic before saving the instance
        logger.info('Saving news instance: %s', self)
        super().save(*args, **kwargs)
