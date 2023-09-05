from django.shortcuts import render

from shelter.models import Breed, Dog


# Create your views here.
def index(request):
    breed_list = Breed.objects.all()[:3]
    context = {'object_list': breed_list, 'title': 'Питомник "Хвост"'}
    return render(request, 'shelter/index.html', context)


def breeds(request):
    full_breed_list = Breed.objects.all()
    context = {'object_list': full_breed_list, 'title': 'Все наши породы'}
    return render(request, 'shelter/breeds.html', context)


def category_dogs(request, pk):
    breed = Breed.objects.get(pk=pk)
    context = {'object_list': Dog.objects.filter(breed_id=pk), 'title': f'Собачки породы {breed.breed}'}
    return render(request, 'shelter/dogs.html', context)

def contact():
    pass