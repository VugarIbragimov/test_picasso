from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import FileSerializer
from rest_framework import generics
from .models import File


class FileUploadView(APIView):
    def post(self, request):
        file_serializer = FileSerializer(data=request.data)

        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(file_serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)


class FileListView(generics.ListAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer
