from django.urls import path
from catalog.views import catalog, product


urlpatterns = [
    path('', catalog),
    path('product/', product)
]