from django.shortcuts import render
from django.views.generic import ListView
from .models import Recipe

class RecipesList(ListView):
    model = Recipe
    template_name = 'recipes/index.html'
    context_object_name = 'recipes'
