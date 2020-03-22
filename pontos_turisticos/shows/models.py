from django.db import models

class Show(models.Model):
    name          = models.CharField(max_length=150)
    description   = models.TextField()
    working_shift = models.TextField()
    min_age       = models.IntegerField()

    def __str__(self):
        return self.nome