from django import forms
from .models import Exercise, BaseExercise
from django_mirror.widgets import MirrorArea


class ExerciseCreateForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = [
            "title",
            "text",
            "solution",
            "tags",
            "topics",
            "note",
            "lecturer",
            "exercise_coordinator",
            "term",
            "university",
            "date",
        ]
        widgets = {
            "date": forms.widgets.DateInput(attrs={"type": "date"}),
            "tags": forms.CheckboxSelectMultiple,
        }


class ExerciseUpdateForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = [
            "title",
            "text",
            "solution",
            "tags",
            "topics",
            "note",
            "date",
            "lecturer",
            "exercise_coordinator",
            "term",
            "university",
        ]


class CommentForm(forms.Form):
    text = forms.CharField(
        widget=MirrorArea(
            attrs={"rows": 20},  # the parent class' attrs still works
        )
    )


class BaseExerciseCreateForm(forms.ModelForm):
    class Meta:
        model = BaseExercise
        fields = ["text"]


class BaseExerciseUpdateForm(forms.ModelForm):
    class Meta:
        model = BaseExercise
        fields = ["text"]
