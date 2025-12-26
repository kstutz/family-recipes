from django.core.validators import MinValueValidator
from django.db import models


class Recipe(models.Model):
    recipe_name = models.CharField(max_length=200)
    source = models.CharField(max_length=200,blank=True, null=True)
    preparation_time = models.CharField(max_length=100)
    cooking_time = models.CharField(max_length=100, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    experimental = models.BooleanField(default=False)
    sweet = models.BooleanField(default=False)
    
    def __str__(self):
        return self.recipe_name
    

class Location(models.Model):
    location_name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.location_name


class Utensil(models.Model):
    utensil_name = models.CharField(max_length=200)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, blank=True, null=True)
    
    def __str__(self):
        return self.utensil_name
   
   
class Instruction(models.Model):
    instruction_text = models.TextField()
    
    def __str__(self):
        return self.instruction_text[:50]


class Step(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    number = models.IntegerField(validators=[MinValueValidator(0)])


class StepInstruction(models.Model):
    step = models.ForeignKey(Step, on_delete=models.CASCADE)
    instruction = models.ForeignKey(Instruction, on_delete=models.CASCADE)
    number = models.IntegerField(validators=[MinValueValidator(0)])
    
    
class RecipeUtensil(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    utensil = models.ForeignKey(Utensil, on_delete=models.CASCADE)


class Ingredient(models.Model):
    ingredient_name = models.CharField(max_length=200)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.ingredient_name


class StepIngredient(models.Model):
    step = models.ForeignKey(Step, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.CharField(max_length=200)
    unit = models.CharField(max_length=100)
    alternatives = models.CharField(max_length=200, blank=True, null=True)


#class IngredientInRecipe(models.Model):
#    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
#    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
#    quantity = models.CharField(max_length=200)
#    unit = models.CharField(max_length=100)
#    alternatives = models.CharField(max_length=200, blank=True, null=True)

    
