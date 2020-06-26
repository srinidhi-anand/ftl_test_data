from django.db import models
from django.contrib.postgres.fields import JSONField, ArrayField
from django.db import models
from django.utils import timezone


class Post(models.Model):
    id = models.CharField(('UUID'), max_length=8, null=False, primary_key=True)
    real_name = models.TextField()
    time = models.TextField()
    # activity_models = ArrayField(models.CharField(max_length=200), blank=True)

    def publish(self):
        self.time = timezone.now()
        self.save()

    def __str__(self):
        return self.real_name

"""
class Members(models.Model):
    
    start_time = models.DateTimeField(auto_now=True)
    end_time = models.DateTimeField(blank = True, null = True)
    activity_models = models.ForeignKey(Post, on_delete=models.CASCADE, null=False)
    def publish(self):
        self.time = timezone.now()
        self.save()

    def __str__(self):
        return self.real_name"""
