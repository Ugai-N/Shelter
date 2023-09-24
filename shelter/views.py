from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView

from shelter.forms import DogForm, ParentForm
from shelter.models import Breed, Dog, Parent


class IndexView(TemplateView):
    template_name = 'shelter/index.html'
    extra_context = {'title': 'Питомник "Хвост"'}

    def get_context_data(self,  **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['object_list'] = Breed.objects.all()[:3]
        return context_data


class BreedListView(ListView):
    model = Breed
    extra_context = {'title': 'Все наши породы'}


class DogListView(ListView):
    model = Dog

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset()
        queryset = queryset.filter(breed_id=self.kwargs.get('pk'))
        return queryset

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        breed_item = Breed.objects.get(pk=self.kwargs.get('pk'))
        context_data['title'] = f'Собачки породы "{breed_item.breed}"'
        return context_data


class DogCreateView(CreateView):
    model = Dog
    form_class = DogForm
    # fields = ('name', 'breed', 'photo', 'birth')

    def get_success_url(self):
        return reverse('shelter:category_dogs', args=[self.object.breed_id])

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        parent_formset = inlineformset_factory(Dog, Parent, form=ParentForm, extra=2)
        if self.request.method == 'POST':
            context_data['formset'] = parent_formset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = parent_formset(instance=self.object)
        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        return super().form_valid(form)


class DogUpdateView(UpdateView):
    model = Dog
    form_class = DogForm
    # fields = ('name', 'breed', 'photo', 'birth')

    def get_success_url(self):
        return reverse('shelter:update_dog', args=[self.object.pk])
    
    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        parent_formset = inlineformset_factory(Dog, Parent, form=ParentForm, extra=2)
        if self.request.method == 'POST':
            context_data['formset'] = parent_formset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = parent_formset(instance=self.object)
        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        return super().form_valid(form)
        


class DogDeleteView(DeleteView):
    model = Dog

    def get_success_url(self):
        return reverse('shelter:category_dogs', args=[self.object.breed_id])


def contact():
    pass