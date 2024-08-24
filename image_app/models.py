from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Image(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image_url = models.URLField()
    description = models.TextField()
    uploaded_at = models.DateTimeField(auto_now_add=True)

class APIMetrics(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    endpoint = models.CharField(max_length=100)
    request_count = models.IntegerField(default=0)
    last_accessed = models.DateTimeField(auto_now=True)

class FunctionMetrics(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    function_name = models.CharField(max_length=100)
    usage_count = models.IntegerField(default=0)
    last_used = models.DateTimeField(auto_now=True)

class AggregateMetrics(models.Model):
    total_api_calls = models.IntegerField(default=0)
    unique_users = models.IntegerField(default=0)
    total_function_calls = models.IntegerField(default=0)