from django.urls import path

from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path(
        "exercise/<int:pk>/", views.ExerciseDetailView.as_view(), name="exercise-detail"
    ),
    path("about/", views.about, name="about"),
    path("exercise/new/", views.ExerciseCreateView.as_view(), name="exercise-create"),
    path(
        "exercise/<int:pk>/update/",
        views.ExerciseUpdateView.as_view(),
        name="exercise-update",
    ),
    path(
        "exercise/<int:pk>/delete/",
        views.ExerciseDeleteView.as_view(),
        name="exercise-delete",
    ),
    path(
        "base-exercise/update/",
        views.BaseExerciseUpdateView.as_view(),
        name="base-exercise-update",
    ),
    path(
        "tag/<str:tag_name>/",
        views.ExerciseTagView,
        name="tag",
    ),
    path(
        "topic/<str:topic_name>/",
        views.ExerciseTopicView,
        name="topic",
    ),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
