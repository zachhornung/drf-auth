from .views import AnimalList, AnimalDetail
from django.urls import path

urlpatterns = [
    path("", AnimalList.as_view(), name="animal_list"),
    path("<int:pk>/", AnimalDetail.as_view(), name="animal_detail"),
]