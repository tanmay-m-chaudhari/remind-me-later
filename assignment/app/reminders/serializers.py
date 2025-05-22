from rest_framework import serializers
from .models import Reminder, ReminderMethodChoices

class ReminderSerializer(serializers.ModelSerializer):
    reminder_method = serializers.ChoiceField(choices=ReminderMethodChoices.choices)

    class Meta:
        model = Reminder
        fields = ['pk', 'message', 'reminder_date', 'reminder_time', 'reminder_method', 'created_at', 'updated_at']
        read_only_fields = ['pk', 'created_at', 'updated_at']