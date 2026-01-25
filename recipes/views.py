from django.shortcuts import render
from django.views import generic
from django_filters.views import FilterView

from .models import Recipe, StepIngredient, RecipeUtensil, Ingredient, Utensil, RecipeFilter, RecipeIngredientFilter


class RecipeFilterView(FilterView):
    model = Recipe
    template_name = 'recipes/index.html'
    filterset_class = RecipeFilter
    context_object_name = 'recipe_list'
    
    
class RecipeIngredientFilterView(FilterView):
    model = Recipe
    template_name = 'recipes/recipes_ingredients.html'
    filterset_class = RecipeIngredientFilter
    context_object_name = 'recipe_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        recipes = context['recipe_list']
        for recipe in recipes:
            steps = recipe.step_set.order_by('number')
            ingredients = []
            for step in steps:
                step.ingredients = StepIngredient.objects.filter(step=step)
                for si in step.ingredients:
                    if si.ingredient not in ingredients:
                        ingredients.append(si.ingredient)
            recipe.ingredients = ingredients
        return context

class IngredientListView(generic.ListView):
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


