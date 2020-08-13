from django.shortcuts import render, HttpResponseRedirect, reverse
from recipe_app.models import Recipe, Author
from recipe_app.forms import AddRecipeForm, AddAuthorForm, LogInForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

# Create your views here.
def main_view(request):
    my_recipes = Recipe.objects.all()
    return render(request, "index.html", {"Recipes": my_recipes, "welcome_name": "Welcome to Recipe Box!"})


def recipe_detail(request, recipe_id):
    my_recipe = Recipe.objects.filter(id=recipe_id).first()
    return render(request, 'recipe_detail.html', {'recipe': my_recipe})

def author_detail(request, author_id):
    my_author = Author.objects.filter(id=author_id).first()
    author_recipes = Recipe.objects.filter(author=my_author.id)
    return render(request, 'author_detail.html', {'author': my_author, 'recipe': author_recipes})

def add_recipe(request):
    if request.method == "POST":
        form = AddRecipeForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Recipe.objects.create(
                title = data.get('title'),
                description = data.get('description'),
                author = data.get('author'),
                time_required = data.get('time_required'),
                ingredients = data.get('ingredients'),
                instructions = data.get('instructions'),
            )
            return HttpResponseRedirect(reverse("homepage"))
        

    form = AddRecipeForm()
    return render(request, "recipe_form.html", {"form": form})

def add_author(request):
    if request.method == "POST":
        form = AddRecipeForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Recipe.objects.create(
                name = data.get('name'),
                bio = data.get('bio'),
            )
            return HttpResponseRedirect(reverse("homepage"))
    form = AddAuthorForm()
    return render(request, "author_form.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        form = LogInForm(request.POST)
            
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data.get("username"), password=data.get("password"))
            if user: 
                login(request, user)
                return HttpResponseRedirect(reverse("homepage"))
            
    form = LogInForm()
    return render(request, "login_form.html", {"form": form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("homepage"))





