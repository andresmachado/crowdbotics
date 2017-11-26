from django import forms

from .models import Dog, Cat

class CatForm(forms.ModelForm):
    class Meta:
        form = Cat
        field = ('name', 'birthday')


class DogForm(forms.ModelForm):
    class Meta:
        form = Dog
        field = ('name', 'birthday')