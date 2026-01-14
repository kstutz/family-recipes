from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

app_name = "recipes"
urlpatterns = [
    # ex: /recipes/
    path("", views.IndexView.as_view(), name="index"),
    # ex: /recipes/list/
    path('list/', views.recipe_list, name="recipe-list"),
    # ex: /recipes/5/
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    # ex: /recipes/utensil/2/
    path("utensil/<int:pk>/", views.UtensilView.as_view(), name="utensil"),
    # ex: /recipes/ingredient/2/
    path("ingredient/<int:pk>/", views.IngredientView.as_view(), name="ingredient"),
]


