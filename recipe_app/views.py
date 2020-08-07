from django.shortcuts import render
from recipe_app.models import Recipe, Author

# Create your views here.
def main_view(request):
    my_recipes = Recipe.objects.all()
    return render(request, "index.html", {"Recipes": my_recipes, "welcome_name": "SE9"})

def author_view(request):
    my_authors = Author.objects.all()
    return render(request, "authors.html", {"Authors": my_authors})

def recipe_view(request):
    return render(request, "recipe.html")

def recipe_detail(request, recipe_id):
    my_recipe = Recipe.objects.filter(id=recipe_id).first()
    return render(request, 'recipe_detail.html', {'recipe': my_recipe})

def author_detail(request, author_id):
    my_author = Author.objects.filter(id=author_id).first()
    author_recipes = Recipe.objects.filter(author=my_author.id)
    return render(request, 'author_detail.html', {'author': my_author, 'recipe': author_recipes})
