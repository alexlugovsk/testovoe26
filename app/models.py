from django.db import models

# Create your models here.
class Fibonachi(models.Model):
    """
    Входные и выходные данные для результатов
    поиска по последовательности Фибоначчи
    """
    input = models.IntegerField()
    output = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.input) + " | " + str(self.output)

    class Meta:
        verbose_name_plural = 'Фибоначи Input/Output'
