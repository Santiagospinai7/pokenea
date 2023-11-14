import factory
import random
from .models import Pokenea

PHOTOS = [
  'https://storage.cloud.google.com/pokenea_teis/pokenea/pokenea1.jpeg',
  'https://storage.cloud.google.com/pokenea_teis/pokenea/pokenea2.jpeg',
  'https://storage.cloud.google.com/pokenea_teis/pokenea/pokenea3.jpeg',
  'https://storage.cloud.google.com/pokenea_teis/pokenea/pokenea4.jpeg',
  'https://storage.cloud.google.com/pokenea_teis/pokenea/pokenea5.jpeg',
  'https://storage.cloud.google.com/pokenea_teis/pokenea/pokenea6.jpeg',
  'https://storage.cloud.google.com/pokenea_teis/pokenea/pokenea7.jpeg',
  'https://storage.cloud.google.com/pokenea_teis/pokenea/pokenea8.jpeg',
  'https://storage.cloud.google.com/pokenea_teis/pokenea/pokenea9.jpeg',
  'https://storage.cloud.google.com/pokenea_teis/pokenea/pokenea10.jpeg',
]

def set_image():
  # I need to get a random photo from the list and then remove it from the list
  photo_selected = random.choice(PHOTOS)
  PHOTOS.remove(photo_selected)
  return photo_selected

class PokeneaFactory(factory.django.DjangoModelFactory):
  class Meta:
    model = Pokenea

  name = factory.Faker('name')
  height = factory.Faker('pyint')
  skill = factory.Faker('word')
  image = factory.LazyFunction(set_image)
  phrase = factory.Faker('sentence')
