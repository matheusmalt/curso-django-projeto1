from django.urls import path
from recipes.views import home, contatcs, about

urlpatterns = [
    path('', home),
    path('contatcs/', contatcs),
    path('about/', about),
]
