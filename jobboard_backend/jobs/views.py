from rest_framework import generics, filters
from .models import Job
from .serializers import JobSerializer
from .permissions import IsAdminOrReadOnly

# Create your views here.
class JobListCreateView(generics.ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'location', 'job_type', 'category__name']

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class JobDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [IsAdminOrReadOnly]