from django.db import models


class Exercise(models.Model):
    name = models.CharField(max_length=30)
    notes = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name}: {self.notes}"


class CardioExercise(Exercise):
    seconds = models.PositiveIntegerField(default=0)


class StrengthExercise(Exercise):
    sets = models.PositiveIntegerField(default=0)
    reps = models.PositiveIntegerField(default=0)
    weight = models.PositiveIntegerField(default=0)


class Food(models.Model):
    name = models.CharField(max_length=30)
    calories = models.IntegerField(default=0)
    notes = models.CharField(max_length=200)
