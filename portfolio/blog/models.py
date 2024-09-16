from django.db import models
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=200)  # Título del artículo
    content = models.TextField()  # Campo donde podrás escribir HTML
    created_at = models.DateTimeField(default=timezone.now)  # Fecha de creación
    updated_at = models.DateTimeField(auto_now=True)  # Fecha de actualización

    def __str__(self):
        return self.title
