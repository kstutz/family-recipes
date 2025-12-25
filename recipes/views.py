from django.views import generic
from .models import Recipe, IngredientInRecipe


class IndexView(generic.ListView):
    template_name = "recipes/index.html"

    def get_queryset(self):
        return Recipe.objects.order_by("recipe_name")[:5]


class DetailView(generic.DetailView):
    model = Recipe

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ingredients'] = IngredientInRecipe.objects.filter(recipe=self.object)
        context['instructions'] = self.object.instruction_set.order_by('step_number')
        return context
