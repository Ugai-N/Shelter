from django.urls import path
from shelter.apps import ShelterConfig
from shelter.views import contact, BreedListView, DogListView, DogCreateView, DogUpdateView, DogDeleteView, IndexView

app_name = ShelterConfig.name

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('contact/', contact, name='contact'),
    path('breeds/', BreedListView.as_view(), name='breeds'),
    path('dogs/<int:pk>', DogListView.as_view(), name='category_dogs'),
    path('dogs/create/', DogCreateView.as_view(), name='create_dog'),
    path('dogs/update/<int:pk>', DogUpdateView.as_view(), name='update_dog'),
    path('dogs/delete/<int:pk>', DogDeleteView.as_view(), name='delete_dog'),
]