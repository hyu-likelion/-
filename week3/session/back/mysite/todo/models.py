from django.db import models

# Create your models here.
class Todolist(models.Model):
    id = models.AutoField(primary_key=True)
    mainText = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    is_approve = models.BooleanField(null=False, default=False)