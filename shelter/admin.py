from django.contrib import admin

from shelter.models import Dog, Breed


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
