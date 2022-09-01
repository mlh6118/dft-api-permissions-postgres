from rest_framework import serializers
from .models import Movie


class MovieSerializer(serializers.ModelSerializer):
    reviewed_by = serializers.CharField(source='reviewer.username')
    reviewer_email = serializers.CharField(source='reviewer.email')

    class Meta:
        fields = ('title', 'stars', 'review', 'reviewed_by',
                  'reviewer_email', 'review_date', 'updated')
        model = Movie
