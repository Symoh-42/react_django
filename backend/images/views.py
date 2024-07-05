from .models import Apple
from .serializers import ApplesSerializer
from rest_framework import generics, status
from rest_framework.response import Response


class ApplesCreate(generics.ListCreateAPIView):
    queryset = Apple.objects.all()
    serializer_class = ApplesSerializer
    
    
    def delete(self, request, *args, **kwargs):
        Apple.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
class ApplesRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Apple.objects.all()
    serializer_class = ApplesSerializer
    lookup_field = "pk"