from django.urls import path
from shelter.apps import ShelterConfig
from shelter.views import index, contact, breeds, category_dogs

app_name = ShelterConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
    path('breeds/', breeds, name='breeds'),
    path('<int:pk>/dogs/', category_dogs, name='category_dogs'),
]