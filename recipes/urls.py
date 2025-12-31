from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

urlpatterns = [
    # ex: /recipes/
    path("", views.IndexView.as_view(), name="index"),
    # ex: /recipes/5/
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    # ex: /recipes/location/2/
    path("location/<int:pk>/", views.LocationView.as_view(), name="location"),
    
]


