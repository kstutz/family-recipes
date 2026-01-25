from django.core.validators import MinValueValidator
from django.db import models
import django_filters


class Recipe(models.Model):
    recipe_name = models.CharField(max_length=200, verbose_name="Rezept")
    source = models.CharField(max_length=200, verbose_name="Quelle", blank=True)
    preparation_time = models.CharField(max_length=100, verbose_name="Zubereitungszeit")
    cooking_time = models.CharField(max_length=100, verbose_name="Koch/Backzeit", blank=True)
    notes = models.TextField(verbose_name="Anmerkungen", blank=True)
    experimental = models.BooleanField(verbose_name="Noch in Erprobung", default=False)
    sweet = models.BooleanField(verbose_name="Süß", default=False)
    
    def __str__(self):
        return self.recipe_name
    

class Location(models.Model):
    location_name = models.CharField(max_length=200, verbose_name="Lagerort", unique=True)
    image = models.ImageField(upload_to="images", verbose_name="Foto", null=True, blank=True)
    
    def __str__(self):
        return self.location_name


class Utensil(models.Model):
    utensil_name = models.CharField(max_length=200, verbose_name="Utensil", unique=True)
    location = models.ForeignKey(Location, verbose_name="Lagerort", on_delete=models.SET_NULL, blank=True, null=True)
    image = models.ImageField(upload_to="images", verbose_name="Foto", null=True, blank=True)
    
    def __str__(self):
        return self.utensil_name
   
   
class Step(models.Model):
    recipe = models.ForeignKey(Recipe, verbose_name="Rezept", on_delete=models.CASCADE)
    number = models.IntegerField(validators=[MinValueValidator(0)])

    
class Instruction(models.Model):
    step = models.ForeignKey(Step, verbose_name="Schritt", on_delete=models.CASCADE)
    text = models.CharField(max_length=400, verbose_name="Text")
    
    
class RecipeUtensil(models.Model):
    recipe = models.ForeignKey(Recipe, verbose_name="Rezept", on_delete=models.CASCADE)
    utensil = models.ForeignKey(Utensil, verbose_name="Utensil", on_delete=models.CASCADE)


class Ingredient(models.Model):
    ingredient_name = models.CharField(max_length=200, verbose_name="Zutat", unique=True)
    location1 = models.ForeignKey(Location, verbose_name="Lagerort", related_name="location1", on_delete=models.SET_NULL, blank=True, null=True)
    location2 = models.ForeignKey(Location, verbose_name="Alternativer Lagerort", related_name="location2", on_delete=models.SET_NULL, blank=True, null=True)
    image = models.ImageField(upload_to="images", verbose_name="Foto", null=True, blank=True)
    usually_stocked = models.BooleanField(default=True, verbose_name="normalerweise vorhanden", )
    alternatives = models.CharField(max_length=200, verbose_name="Mögliche Alternative(n)", blank=True)

    def __str__(self):
        return self.ingredient_name


class StepIngredient(models.Model):
    step = models.ForeignKey(Step, verbose_name="Schritt", on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, verbose_name="Zutat", on_delete=models.CASCADE)
    quantity = models.CharField(max_length=200, verbose_name="Menge")
    unit = models.CharField(max_length=100, verbose_name="Einheit", blank=True)
    alternatives = models.CharField(max_length=200, verbose_name="Mögliche Alternative(n)", blank=True)

    def __str__(self):
        return self.ingredient.ingredient_name
    
    
class RecipeFilter(django_filters.FilterSet):
    class Meta:
        model = Recipe
        fields = ['sweet', 'experimental']
        
        
class RecipeIngredientFilter(django_filters.FilterSet):
    ingredient = django_filters.ModelChoiceFilter(queryset=Ingredient.objects.all(),
                                                  field_name='step__stepingredient__ingredient', label='Zutat')

    class Meta:
        model = Recipe
        fields = ['ingredient']
