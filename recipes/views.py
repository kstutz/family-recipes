from django.views import generic
from .models import Recipe, StepIngredient, RecipeUtensil


class IndexView(generic.ListView):
    template_name = "recipes/index.html"

    def get_queryset(self):
        return Recipe.objects.order_by("recipe_name")[:5]


class DetailView(generic.DetailView):
    model = Recipe

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        steps = self.object.step_set.order_by('number')
        for step in steps:
            step.ingredients = StepIngredient.objects.filter(step=step)
        context['steps'] = steps
#        context['instructions'] = self.object.instruction_set.order_by('step_number')
#        context['utensils'] = self.object.recipeutensil_set.all()
        context['utensils'] = RecipeUtensil.objects.filter(recipe=self.object)
        return context
