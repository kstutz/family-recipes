from django.urls import path

from . import views

urlpatterns = [
    # ex: /recipes/
    path("", views.IndexView.as_view(), name="index"),
    # ex: /recipes/5/
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
]


