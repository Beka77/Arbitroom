from django.db import models

# Create your models here.
class Setting(models.Model):
    title = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='logo/')
    descriptiom = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Настройка'
        verbose_name_plural = 'Настройки'