from django.urls import path

from api.views import FavoritesPhoto, FavoritesAlbum

app_name = 'api'
urlpatterns = [
    path('photo/favorites/<int:pk>/', FavoritesPhoto.as_view(), name='favorite'),
    path('album/favorites/<int:pk>/', FavoritesAlbum.as_view(), name='favorite_album'),
]