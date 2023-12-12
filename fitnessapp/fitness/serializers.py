from rest_framework import serializers
from .models import Exercise, Food


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = ("id", "name", "notes")


class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = ("id", "name", "calories", "notes")
