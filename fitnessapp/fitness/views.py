from rest_framework import viewsets
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from .models import Exercise
from .serializers import ExerciseSerializer


class ExercisesViewSet(viewsets.ModelViewSet):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
    allowed_methods = ["GET", "POST", "DELETE"]
