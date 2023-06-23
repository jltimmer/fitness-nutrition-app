from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from .models import Exercise
from .serializers import ExerciseSerializer

@api_view(['GET', 'POST'])
def index(request):
	if request.method == 'GET':
		data = Exercise.objects.all()
		serializer = ExerciseSerializer(data, context={'request': request}, many=True)
		return Response(serializer.data)

	elif request.method == 'POST':
		data = JSONParser().parse(request)
		serializer = ExerciseSerializer(data=data, context={'request': request})
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=201)
		return Response(serializer.erros, status=400)
