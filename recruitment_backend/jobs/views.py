from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView
from .models import Application, Job
from .serializers import JobSerializer, ApplicationSerializer

class JobListCreateView(generics.ListCreateAPIView):  # ✅ Change from CreateAPIView
    queryset = Job.objects.all()
    serializer_class = JobSerializer

class ApplicationCreateView(generics.ListCreateAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    parser_classes = (MultiPartParser, FormParser)  # Enable file uploads

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ApplicationListView(generics.ListAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
