from django.urls import path
from . import views


urlpatterns = [
    path('', views.all_animal_view, name='all_animals'),
    path('<int:id>/', views.animal_view, name='animal'),


]
