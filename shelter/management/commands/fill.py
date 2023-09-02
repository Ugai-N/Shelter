from django.core.management import BaseCommand

from shelter.models import Dog, Breed


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        dogs_list = [{
                          "name": "Тимон",
                          "breed": Breed(3),
                          "photo": "",
                          "birth": None
                        },
                       {
                            "name": "Пумба",
                            "breed": Breed(3),
                            "photo": "",
                            "birth": None
                        }]

        dogs_to_add = []
        for dog in dogs_list:
            dogs_to_add.append(Dog(**dog))
        Dog.objects.bulk_create(dogs_to_add)
