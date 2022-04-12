from django.db import models
class User(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=255)


    def __str__(self) -> str:
        return self.name