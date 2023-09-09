from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView

from shelter.models import Breed, Dog


class IndexView(TemplateView):
    template_name = 'shelter/index.html'
    extra_context = {'title': 'Питомник "Хвост"'}

    def get_context_data(self,  **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['object_list'] = Breed.objects.all()[:3]
        return context_data

#
# def index(request):
#     breed_list = Breed.objects.all()[:3]
#     context = {'object_list': breed_list, 'title': 'Питомник "Хвост"'}
#     return render(request, 'shelter/index.html', context)


class BreedListView(ListView):
    model = Breed
    extra_context = {'title': 'Все наши породы'}


# def breeds(request):
#     full_breed_list = Breed.objects.all()
#     context = {'object_list': full_breed_list, 'title': 'Все наши породы'}
#     return render(request, 'shelter/breed_list.html', context)

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


# Breed.breed(pk=self.kwargs.get('pk'))
# def category_dogs(request, pk):
#     breed = Breed.objects.get(pk=pk)
#     context = {'object_list': Dog.objects.filter(breed_id=pk), 'title': f'Собачки породы {breed.breed}'}
#     return render(request, 'shelter/dog_list.html', context)


class DogCreateView(CreateView):
    model = Dog
    fields = ('name', 'breed', 'photo', 'birth')
    # success_url = reverse_lazy('shelter:index')
    # success_url = reverse_lazy('shelter:category_dogs')

    def get_success_url(self):
        return reverse('shelter:category_dogs', args=[self.object.breed_id])


class DogUpdateView(UpdateView):
    model = Dog
    fields = ('name', 'breed', 'photo', 'birth')
    # success_url = reverse_lazy('shelter:index')

    def get_success_url(self):
        return reverse('shelter:category_dogs', args=[self.object.breed_id])


class DogDeleteView(DeleteView):
    model = Dog

    def get_success_url(self):
        return reverse('shelter:category_dogs', args=[self.object.breed_id])

    # def get_context_data(self, *args, **kwargs):
    #     context_data = super().get_context_data(*args, **kwargs)
    #     breed_item = Breed.objects.get(pk=self.kwargs.get('breed_id'))
    #     context_data['breed_PK'] = breed_item.pk
    #     return context_data


def contact():
    pass