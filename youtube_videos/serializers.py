from rest_framework import serializers
from .models import Video

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ["id", "title", "description", "publishing_date", "thumbnail_urls", "view_count", "duration"]
