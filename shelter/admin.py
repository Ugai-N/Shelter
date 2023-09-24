from django.contrib import admin

from shelter.models import Dog, Breed, Parent


# Register your models here.
@admin.register(Dog)
class DogAdmin(admin.ModelAdmin):
    list_display = ('name', 'breed', 'birth', 'photo')
    list_filter = ('breed',)
    search_fields = ('name',)


@admin.register(Breed)
class BreedAdmin(admin.ModelAdmin):
    list_display = ('pk', 'breed', 'description')
    search_fields = ('breed',)


@admin.register(Parent)
class ParentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'breed', 'birth', 'dog')
    list_filter = ('dog',)
