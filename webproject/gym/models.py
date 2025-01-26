from django.db import models
from django.contrib.auth.models import User

# Abstract base model for date tracking
class AppModel(models.Model):
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

# Muscle group for exercises
class MuscleGroup(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

# Abstract Exercise model
class Exercise(AppModel):
    name = models.CharField(max_length=100, null=True)
    equipment = models.CharField(max_length=50, blank=True, null=True)
    target_muscles = models.ForeignKey(MuscleGroup, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

class WorkoutPreset(models.Model):
    name = models.CharField(max_length=100, null=True)  # Name of the workout (e.g., "Leg Day")
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)  # Each workout belongs to a user
    exercises = models.ManyToManyField(Exercise, through='WorkoutExercise')  # Link to multiple exercises

    def __str__(self):
        return self.name

# Workout model linked to User
class Workout(AppModel):
    date = models.DateField()  # Date of the workout
    satisfaction = models.PositiveSmallIntegerField()  # Satisfaction rating from 1-10
    workout_type = models.ForeignKey(WorkoutPreset, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.satisfaction} ({self.date})"

# Link between workout and exercises with sets
class WorkoutExercise(models.Model):
    workout_preset = models.ForeignKey(WorkoutPreset, on_delete=models.CASCADE, null=True)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, null=True)

class ExerciseSet(models.Model):

    workout_exercise = models.ForeignKey(WorkoutExercise, on_delete=models.CASCADE, related_name='sets')
    set_number = models.PositiveSmallIntegerField(default=1, blank=True, null=True)

    def __str__(self):
        return f"Set: {self.set_number} - "

class Rep (models.Model):

    set = models.ForeignKey(ExerciseSet, on_delete=models.CASCADE, related_name="reps")
    weight = models.DecimalField(decimal_places=2, max_digits=5)

    def __str__(self):
        return f"Rep: {self.pk} - Total weight: {self.weight}"