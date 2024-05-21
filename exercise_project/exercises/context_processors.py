from .models import Tag, Topic


def custom_data(request):
    # Define the data you want to provide to all views

    tags = Tag.objects.all()
    topics = Topic.objects.all()

    data = {"tags_list": tags, "topics_list": topics}
    return data
