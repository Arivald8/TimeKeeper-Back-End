from django.db import models

class Activity(models.Model):
    activity_name = models.CharField(max_length=200, blank=False)
    activity_duration = models.CharField(max_length=300, blank=False)
    activity_date = models.DateField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return f"Activity: {self.activity_name} Started at: {self.activity_start} Activity Duration: {self.activity_duration}"

