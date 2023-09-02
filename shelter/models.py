from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Dog(models.Model):
    name = models.CharField(max_length=250, verbose_name='кличка')
    breed = models.ForeignKey('Breed', on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='photo/', verbose_name='фото', **NULLABLE)
    birth = models.DateField(verbose_name='ДР', **NULLABLE)

    def __str__(self):
        return f'{self.name} ({self.breed})'

    class Meta:
        verbose_name = 'собака'
        verbose_name_plural = 'собаки'
        ordering = ('name', 'breed',)


class Breed(models.Model):
    breed = models.CharField(max_length=250, verbose_name='порода')
    description = models.CharField(max_length=250, verbose_name='Описание', **NULLABLE)

    def __str__(self):
        return f'{self.breed}'

    class Meta:
        verbose_name = 'порода'
        verbose_name_plural = 'породы'