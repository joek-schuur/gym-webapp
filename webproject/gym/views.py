from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import *

@login_required
def create_workout_preset(request):
    if request.method == 'POST':
        workout_preset_form = WorkoutPresetForm(request.POST)
        workout_preset_exercise_form = WorkoutPresetExerciseForm(request.POST)

        if workout_preset_form.is_valid() and workout_preset_exercise_form.is_valid():
            workout_preset = workout_preset_form.save(commit=False)
            workout_preset_exercise = workout_preset_exercise_form.save(commit=False)
            workout_preset.user = request.user
            workout_preset.save()
            workout_preset_exercise.save()

            return redirect('homepage')  # Redirect after successful save

    else:
        workout_preset_form = WorkoutPresetForm()
        workout_preset_exercise_form = WorkoutPresetExerciseForm()

    return render(request, 'gym/create_preset.html', {
        'workout_preset_form': workout_preset_form,
        'exercise_forms': workout_preset_exercise_form,
    })

@login_required
def log_workout(request):
    if request.method == 'POST':
        workout_form = WorkoutForm(request.POST)
        set_formset = SetFormSet(request.POST)
        rep_formset = RepFormSet(request.POST)

        if workout_form.is_valid() and set_formset.is_valid() and rep_formset.is_valid():
            workout = workout_form.save(commit=False)
            workout.user = request.user  # Assign logged in user
            workout.save()

            set_formset = workout.save(commit=False)
            set_formset.instance = workout
            set_formset.save()

            rep_formset = set_formset.save(commit=False)
            rep_formset.instance = set_formset
            rep_formset.save()

            return redirect('homepage')  # Redirect after successful save
    else:
        workout_form = WorkoutForm()
        set_formset = SetFormSet()
        rep_formset = RepFormSet()

    return render(request, 'gym/log_workout.html', {
        'workout_form': workout_form,
        'set_formset': set_formset,
        'rep_formset': rep_formset,
    })

def homepage(request):
    return render(request, "gym/homepage.html")

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
    else:
        form = CustomUserCreationForm()
    
    return render(request, "gym/register.html", { "form" : form })





