from rest_framework import serializers
from .models import Bug


# Serializers

class BugSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bug
        fields = ('pk', 'category', 'view_status', 'priority', 'resolution', 'severity',
                  'created_on', 'updated_on', 'author', 'assigned_to', 'project', 'summary', 'description')
