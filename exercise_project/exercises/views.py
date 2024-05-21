from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
    View,
)
import os
from .utils import convert_pdf_to_png
from pprint import pprint

from .forms import (
    ExerciseCreateForm,
    CommentForm,
    ExerciseUpdateForm,
    BaseExerciseUpdateForm,
)
from .models import Exercise, BaseExercise, Tag, Topic


class IndexView(ListView):
    template_name = "exercises/index.html"
    context_object_name = "exercise_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Exercise.objects.order_by("-date")


class ExerciseDetailView(DetailView):
    model = Exercise


class ExerciseCreateView(CreateView):
    model = Exercise
    form_class = ExerciseCreateForm


class ExerciseUpdateView(UpdateView):
    model = Exercise
    form_class = ExerciseUpdateForm
    template_name = "exercises/exercise_form.html"
    extra_context = {"title": "Update Exercise"}


class ExerciseDeleteView(DeleteView):
    model = Exercise
    success_url = reverse_lazy("index")


def about(request):
    return render(request, "exercises/about.html", {"title": "About"})


def test(request):
    if request.POST:
        form = CommentForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data["text"]
            with open("media/pdfs/main.tex", "w") as f:
                f.write(text)

            os.system("pdflatex -output-directory media/pdfs/ media/pdfs/main.tex")

            convert_pdf_to_png("media/pdfs/main.pdf", "media/pngs/")
    else:
        form = CommentForm()
    return render(request, "exercises/test.html", {"title": "test", "form": form})


# def ExerciseUpdateView(request, pk):
#     exercise = get_object_or_404(Exercise, pk=pk)
#     base_exercise = get_object_or_404(BaseExercise, pk=1)
#     if request.POST:
#         form = ExerciseCreateForm(request.POST, instance=exercise)
#         if form.is_valid():
#             text = form.cleaned_data["text"]
#             # merged_exercise = base_exercise.text.replace(
#             #     "{% block exercise %}{% endblock %}", text
#             # )
#             # with open("media/pdfs/main.tex", "w") as f:
#             #     f.write(merged_exercise)

#             # os.system("pdflatex -output-directory media/pdfs/ media/pdfs/main.tex")

#             # convert_pdf_to_png("media/pdfs/main.pdf", f"media/pngs/exercise_{pk}.png")

#             # exercise.png_file = f"pngs/exercise_{pk}.png"
#             form.save()

#             return redirect("exercise-detail", pk=pk)
#     else:
#         form = ExerciseCreateForm(instance=exercise)
#     return render(
#         request, "exercises/exercise_form.html", {"title": "test", "form": form}
#     )


class BaseExerciseUpdateView(View):
    template_name = "exercises/baseexercise_form.html"

    def get(self, request):
        base_exercise = get_object_or_404(BaseExercise, pk=1)
        form = BaseExerciseUpdateForm(instance=base_exercise)
        return render(
            request, self.template_name, {"title": "Update Base Exercise", "form": form}
        )

    def post(self, request):
        base_exercise = get_object_or_404(BaseExercise, pk=1)
        form = BaseExerciseUpdateForm(request.POST, instance=base_exercise)
        if form.is_valid():
            form.save()
            return redirect(self.template_name)

        return render(
            request, self.template_name, {"title": "Update Base Exercise", "form": form}
        )


def ExerciseTagView(request, tag_name):
    tag = get_object_or_404(Tag, title=tag_name)
    exercise_list = Exercise.objects.filter(tags=tag)

    context = {
        "title": "test",
        "exercise_list": exercise_list,
    }

    return render(request, "exercises/index.html", context)


def ExerciseTopicView(request, topic_name):
    topic = get_object_or_404(Topic, title=topic_name)
    exercise_list = Exercise.objects.filter(topics=topic)

    context = {
        "title": "test",
        "exercise_list": exercise_list,
    }
    return render(request, "exercises/index.html", context)
