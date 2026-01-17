from django.shortcuts import render
from django.views import generic
from .models import Recipe, StepIngredient, RecipeUtensil, Location, Ingredient, Utensil, RecipeFilter


class IndexView(generic.ListView):
    template_name = "recipes/ingredient_list.html"

    def get_queryset(self):
        return Ingredient.objects.order_by("ingredient_name")


class DetailView(generic.DetailView):
    model = Recipe

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        steps = self.object.step_set.order_by('number')
        for step in steps:
            step.ingredients = StepIngredient.objects.filter(step=step)
            step.instructions = step.instruction_set.order_by('id')
        context['steps'] = steps
#        context['instructions'] = self.object.instruction_set.order_by('step_number')
#        context['utensils'] = self.object.recipeutensil_set.all()
        context['utensils'] = RecipeUtensil.objects.filter(recipe=self.object)
        return context


class IngredientView(generic.DetailView):
    model = Ingredient


class UtensilView(generic.DetailView):
    model = Utensil


def recipe_list(request):
    f = RecipeFilter(request.GET, queryset=Recipe.objects.all())
    return render(request, 'recipes/index.html', {'filter': f})