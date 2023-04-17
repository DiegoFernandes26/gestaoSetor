from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Tarefa(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    concluida = models.BooleanField(default=False)
    created_user_id = models.ForeignKey(User, on_delete=models.CASCADE())
    create_date = models.DateTimeField(auto_now_add=True)

