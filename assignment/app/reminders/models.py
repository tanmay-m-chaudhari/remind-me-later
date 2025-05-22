from django.db import models
from .model_choices import ReminderMethodChoices

# Create your models here.
class Reminder(models.Model):
    message = models.TextField()
    reminder_date = models.DateField()
    reminder_time = models.TimeField()
    reminder_method = models.CharField(
        max_length=10,
        choices=ReminderMethodChoices.choices,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Reminder for {self.remind_date} at {self.remind_time} via {self.remind_method}: {self.message[:50]}..."
