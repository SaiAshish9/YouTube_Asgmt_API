from .models  import Video
from .serializers import VideoSerializer
from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.mixins import ListModelMixin
from rest_framework.filters import SearchFilter

class VideotList(GenericAPIView, ListModelMixin):
    queryset = Video.objects.all().order_by('-publishing_date')
    serializer_class = VideoSerializer
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
class VideoSearchView(ListAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    filter_backends = [SearchFilter]
    search_fields = ['title', 'description']