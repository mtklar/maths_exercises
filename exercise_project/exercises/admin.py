from django.contrib import admin
from django_mirror.admin import MirrorAdmin
from .models import Exercise, BaseExercise, Tag, Topic


@admin.register(Exercise)
class CommentAdmin(MirrorAdmin, admin.ModelAdmin):
    mirror_fields = (  # with custom options
        (
            "text",
            {
                "mode": "stex",
                "line_wrapping": True,
            },
        ),
    )


@admin.register(BaseExercise)
class CommentAdmin(MirrorAdmin, admin.ModelAdmin):
    mirror_fields = (  # with custom options
        (
            "text",
            {
                "mode": "stex",
                "line_wrapping": True,
            },
        ),
    )


@admin.register(Tag)
class CommentAdmin(MirrorAdmin, admin.ModelAdmin):
    pass


@admin.register(Topic)
class CommentAdmin(MirrorAdmin, admin.ModelAdmin):
    pass
