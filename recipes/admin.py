from django.contrib import admin

from .models import Recipe, IngredientInRecipe, Ingredient, Location, Instruction, RecipeUtensil, Utensil


class IngredientInline(admin.StackedInline):
    model = IngredientInRecipe
    extra = 1


class InstructionInline(admin.StackedInline):
    model = Instruction
    extra = 1
    
    
class UtensilInline(admin.StackedInline):
    model = RecipeUtensil
    extra = 1


class RecipeAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["recipe_name"]}),
        ("Other information", {"fields": ["preparation_time", "cooking_time", "source", "notes"], "classes": ["collapse"]}),
    ]
    inlines = [IngredientInline, UtensilInline, InstructionInline]
    
    
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient)
admin.site.register(Utensil)
admin.site.register(Location)