from django.db import models

# Create your models here.
class Clases(models.Model):
    teacher = models.CharField(max_length=32)
    topic = models.CharField(max_length=32)

    class Meta:
        verbose_name = 'Clase'
        verbose_name_plural = 'Clases'

    def __str__(self) -> str:
        return f'{self.topic} - {self.teacher}'