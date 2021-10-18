from django.urls import path

from .views import detail, room, new

urlpatterns = [
    path('<int:id>', detail, name="detail"),
    path('rooms', room, name="rooms"),
    path('new', new, name="new")
]