from .models  import Video
from .serializers import VideoSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin

class VideotList(GenericAPIView, ListModelMixin):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)