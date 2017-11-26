from django.views.generic import ListView
from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .models import Cat, Dog

# Create your views here.


def home(request):
    return render(request, 'home.html', {})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


class DogList(ListView):
    model = Dog
    queryset = Dog.objects.all()

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)


class DogCreate(CreateView):
    model = Dog
    fields = ('name', 'birthday')
    success_url = reverse_lazy('dog-list')
    
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.owner = self.request.user
        obj.save()
        return super(DogCreate, self).form_valid(form)

class CatList(ListView):
    model = Cat
    queryset = Cat.objects.all()

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)


class CatCreate(CreateView):
    model = Cat
    fields = ('name', 'birthday')
    success_url = reverse_lazy('cat-list')

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.owner = self.request.user
        obj.save()
        return super(CatCreate, self).form_valid(form)
