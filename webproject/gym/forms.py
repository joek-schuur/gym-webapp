from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.models import User
from django import forms
from .models import Workout, WorkoutExercise, Rep, ExerciseSet, WorkoutPreset, Exercise

class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ['date', 'satisfaction']

class SetFormSet(forms.ModelForm):
    class Meta:
        model = ExerciseSet
        fields = ['set_number']
        widgets = {
            "set_number": forms.HiddenInput,
        }
        field_classes = {
            "set_number": forms.IntegerField,
        }

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['set_number'].label = 1

class RepFormSet(forms.ModelForm):
    class Meta:
        model = Rep
        fields = ['weight'] ## pk = 1 --- weight = ...kg

class CustomUserCreationForm(UserCreationForm):

    error_messages = {
        'password_mismatch': ("Passwords didn't match."),
    }

    username = forms.CharField(
        label = ("Username"),
        widget = forms.TextInput ( attrs= 
            {
            'class': "form-control",
            'style': 'max-width: 300px;',
            'placeholder': 'Username'
            } ),
        required = True, 
        max_length = 30,
        )
    
    email = forms.EmailField(
        label = ("Email"),
        widget = forms.EmailInput ( attrs= 
            {
            'class': "form-control",
            'style': 'max-width: 300px;',
            'placeholder': 'Email'
            } ),
        required = True,
        )

    password1 = forms.CharField(
        label = ("Password"),
        widget = forms.PasswordInput ( attrs= 
            {
            'class': "form-control",
            'style': 'max-width: 300px;',
            'placeholder': 'Password'
            } ),
        required = True, 
        )
    
    password2 = forms.CharField(
        label = ("Confirm password"),
        widget=forms.PasswordInput ( attrs= 
            {
            'class': "form-control",
            'style': 'max-width: 300px;',
            'placeholder': 'Confirm Password'
            } ),
        required = True, 
        )
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class CustomAuthenticationForm(AuthenticationForm):

    username = UsernameField(
        widget=forms.TextInput(attrs=
            { "autofocus": True,
            'class': "form-control",
            'style': 'max-width: 300px;',
            'placeholder': 'Username/Email'
            } ),
        label="Username or Email",
        )
    
    password = forms.CharField(
        label=("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs=
            {"autocomplete": "current-password",
            'class': "form-control",
            'style': 'max-width: 300px;',
            'placeholder': 'Password'
            } ),
        )

class WorkoutPresetForm(forms.Form):
    name = forms.CharField(
        required=True,
        label="Name of this workout",
        widget=forms.TextInput(attrs=
            {
            'class': "form-control",
            'style': 'max-width: 300px;',
            'placeholder': 'Name'
            } ),
        )

class WorkoutPresetExerciseForm(forms.ModelForm):
    class Meta:
        model = WorkoutExercise
        exclude = ['workout_preset']
    
    EXERCISES = Exercise.objects.all()
    CHOICES = ((exercise.pk, exercise.name) for exercise in EXERCISES)
    exercise = forms.ChoiceField(
        choices=CHOICES,
        label=("Exercise"),
        widget=forms.Select(attrs=
            {
            'style': "max-width: 300px;",
            'class' : "exercise-choice"
            } ),
        )
    
WorkoutPresetExerciseForm = forms.inlineformset_factory(WorkoutPreset, WorkoutExercise, WorkoutPresetExerciseForm, extra=1, can_delete=False)
SetFormSet = forms.inlineformset_factory(WorkoutExercise, ExerciseSet, form=SetFormSet, extra=0, can_delete=True)
RepFormSet = forms.inlineformset_factory(ExerciseSet, Rep, form=RepFormSet, extra=8, can_delete=True)