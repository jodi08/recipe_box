from django.shortcuts import render
from recipe_app.models import Recipes

# Create your views here.
def main_view(request):
    my_recipes = Recipes.objects.all()
    return render(request, "index.html", {"Recipes": my_recipes, })

def author_view(request):
    return render(request, "authors.html")

def recipe_view(request):
    return render(request, "recipe.html")