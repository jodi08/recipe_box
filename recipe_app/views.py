from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.admin.views.decorators import staff_member_required


from recipe_app.forms import AddRecipeForm, AddAuthorForm, LogInForm
from recipe_app.models import Recipe, Author

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

@staff_member_required
@login_required
def recipe_edit_view(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    if request.method == "POST":
        form = AddRecipeForm(request.POST)
        if form.is_valid():
            data=form.cleaned_data
            recipe.title = data['title']
            recipe.description = data['description']
            recipe.time_required = data['time_required']
            recipe.ingredients = data['ingredients']
            recipe.instructions = data['instructions']
            recipe.save()
        return HttpResponseRedirect(reverse("recipe_detail", args=[recipe.id]))
    
    data = {
        "title": recipe.title,
       "description": recipe.description,
       "time_required": recipe.time_required,
       "ingredients": recipe.ingredients,
       "instructions": recipe.instructions
    }

    form = AddRecipeForm(initial=data)
    return render(request, "recipe_form.html", {"form": form})

@login_required
def add_recipe(request):
    if request.method == "POST":
        form = AddRecipeForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Recipe.objects.create(
                title = data.get('title'),
                description = data.get('description'),
                author = request.user.author,
                time_required = data.get('time_required'),
                ingredients = data.get('ingredients'),
                instructions = data.get('instructions'),
            )
            return HttpResponseRedirect(reverse("homepage"))
        

    form = AddRecipeForm()
    return render(request, "recipe_form.html", {"form": form})

@login_required
def favorite(request, pk):
    my_recipe = Recipe.objects.get(id=pk)
    my_user = Author.objects.get(user=request.user)
    my_user.favorites.add(my_recipe)
    my_user.save()
    print(my_user.favorites.all())
    return HttpResponseRedirect(reverse('homepage'))
    # return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@staff_member_required
@login_required
def add_author(request):
    if request.method == "POST":
        form = AddAuthorForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_user = User.objects.create_user(username=data.get("username"), password=data.get("password"))
            Author.objects.create(name=data.get("username"), user=new_user)
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
                return HttpResponseRedirect(request.GET.get('next', reverse("homepage")))
            
    form = LogInForm()
    return render(request, "login_form.html", {"form": form})

def signup_view(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_user = User.objects.create_user(username=data.get("username"), password=data.get("password"))
            Author.objects.create(name=data.get("username"), user=new_user)
            login(request, new_user)
            return HttpResponseRedirect(reverse("homepage"))

    form = SignUpForm()
    return render(request, 'signup_form.html', {"form": form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("homepage"))







