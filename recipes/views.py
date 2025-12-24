from django.views import generic
from .models import Recipe


class IndexView(generic.ListView):
    template_name = "recipes/index.html"

    def get_queryset(self):
        return Recipe.objects.order_by("recipe_name")[:5]


class DetailView(generic.DetailView):
    model = Recipe
