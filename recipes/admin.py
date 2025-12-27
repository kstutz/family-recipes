from django.contrib import admin
import nested_admin

from .models import Recipe, Step, Ingredient, Location, RecipeUtensil, Utensil, StepIngredient, Instruction


class StepIngredientInline(nested_admin.NestedStackedInline):
    model = StepIngredient
    extra = 1


class InstructionInline(nested_admin.NestedStackedInline):
    model = Instruction
    extra = 1
    
    
class StepInline(nested_admin.NestedStackedInline):
    model = Step
    extra = 1
    inlines = [StepIngredientInline, InstructionInline]

    
class UtensilInline(nested_admin.NestedStackedInline):
    model = RecipeUtensil
    extra = 1


class RecipeAdmin(nested_admin.NestedModelAdmin):
    fieldsets = [
        (None, {"fields": ["recipe_name"]}),
        ("Other information", {"fields": ["preparation_time", "cooking_time", "source", "notes",  "sweet", "experimental"],
                               "classes": ["collapse"]}),
    ]
    inlines = [UtensilInline, StepInline]


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient)
admin.site.register(Utensil)
admin.site.register(Location)