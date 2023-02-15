from django.db import models

class Exercise(models.Model):
	name = models.CharField(max_length=30)
	notes = models.CharField(max_length=200)

class CardioExercise(Exercise):
    seconds = models.PositiveIntegerField(default=0)
    
class StrengthExercise(Exercise):
    sets = models.PositiveIntegerField(default=0)
    reps = models.PositiveIntegerField(default=0)
    weight = models.PositiveIntegerField(default=0)
