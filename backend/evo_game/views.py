from rest_framework import viewsets
from .models import Population
from .serializers import PopSerializer

class PopViewSet(viewsets.ModelViewSet):
    queryset = Population.objects.all()
    serializer_class = PopSerializer
