from django.db import models
from django.urls import reverse


class Tag(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Topic(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Exercise(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    solution = models.TextField()
    lecturer = models.CharField(max_length=200)
    exercise_coordinator = models.CharField(max_length=200)
    date = models.DateField("date created")
    term = models.CharField(max_length=200)
    university = models.CharField(max_length=200, default="TUM")
    pdf_file = models.FileField(upload_to="pdfs/")
    png_file = models.ImageField(upload_to="pngs/")
    tags = models.ManyToManyField(Tag)
    topics = models.ManyToManyField(Topic)
    note = models.TextField(blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("exercise-detail", kwargs={"pk": self.pk})


class BaseExercise(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    png_file = models.ImageField(upload_to="pngs/")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("base-exercise-update", kwargs={"pk": self.pk})
