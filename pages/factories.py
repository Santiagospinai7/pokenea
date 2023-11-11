import factory
from .models import Pokenea

class PokeneaFactory(factory.django.DjangoModelFactory):
  class Meta:
    model = Pokenea

  name = factory.Faker('name')
  height = factory.Faker('pyint')
  skill = factory.Faker('word')
  image = factory.Faker('image_url')
  phrase = factory.Faker('sentence')
