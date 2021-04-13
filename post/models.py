from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    content = models.TextField("post contents")
    created_on = models.DateTimeField("creation time", default=timezone.now, db_index=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.content} - {self.created_on}"

    def get_absolute_url(self):
        # TO-DO
        pass