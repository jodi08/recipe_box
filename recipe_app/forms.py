from django import forms
from recipe_app.models import Recipe, Author

class AddRecipeForm(forms.Form):
    title = forms.CharField(max_length=100)
    author = forms.ModelChoiceField(queryset=Author.objects.all())
    description = forms.CharField(max_length=100)
    time_required = forms.CharField(max_length=25)
    ingredients = forms.CharField(widget=forms.Textarea)
    instructions = forms.CharField(widget=forms.Textarea)


class AddAuthorForm(forms.Form):
    name = forms.CharField(max_length = 50)
    bio = forms.CharField(widget=forms.Textarea)
    username = forms.CharField(max_length=240, initial="")
    password = forms.CharField(widget=forms.PasswordInput, initial="")

class LogInForm(forms.Form):
    username = forms.CharField(max_length=240, initial="")
    password = forms.CharField(widget=forms.PasswordInput, initial="")


    
