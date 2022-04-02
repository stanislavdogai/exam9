from django.urls import path

from api.views import FavoritesPhoto

app_name = 'api'
urlpatterns = [
    path('photo/favorites/<int:pk>/', FavoritesPhoto.as_view(), name='favorite')
]