from rest_framework import serializers
from .models import Activity
from rest_framework.reverse import reverse

class ActivityListSerializer(serializers.ModelSerializer):
    absolute_url = serializers.SerializerMethodField()

    class Meta:
        model = Activity
        fields = [
            'activity_name',
            'activity_duration',
            'activity_date',
            'absolute_url'
        ]
    
    def get_absolute_url(self, obj):
        return reverse('activities_detail', args=(obj.pk,))


