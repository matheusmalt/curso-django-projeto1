from faker import Faker
from random import randint

fake = Faker('pt_BR')

def make_recipe():
    return { 
        'title': fake.sentence(),
        'description':  fake.sentence(nb_words= 12),
        'preparation_time':  randint(1, 100),
        'preparation_time_unit': 'Minutos',
        'servings':  randint(1, 100),
        'servings_unit': 'Porção',
        'preparation_steps':  fake.text(randint(100, 3000)),
        'created_at': fake.date_time(),
        'author': {
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
        },
        'category': fake.sentence(nb_words=randint(1,2)),
        'cover': {
            'url': f'https://loremflickr.com/1280/720/food,cook'
        }
}

print(make_recipe())