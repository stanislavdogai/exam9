from django.urls import path

from webapp.views.albums import AlbumDetailView, AlbumCreateView, AlbumDeleteView, AlbumUpdateView
from webapp.views.photos import PhotoIndexView, PhotoCreateView, PhotoDetailView, PhotoDeleteView, PhotoUpdateView, \
    PhotoTokenDetailView, PhotoTokenGenerate

app_name = 'webapp'
urlpatterns = [
    path('', PhotoIndexView.as_view(), name='photo_index'),
    path('create/', PhotoCreateView.as_view(), name='photo_create'),
    path('detail/<int:pk>/', PhotoDetailView.as_view(), name='photo_detail'),
    path('delete/<int:pk>/', PhotoDeleteView.as_view(), name='photo_delete'),
    path('update/<int:pk>/', PhotoUpdateView.as_view(), name='photo_update'),
    path('album/<int:pk>/', AlbumDetailView.as_view(), name='album_view'),
    path('album/create/', AlbumCreateView.as_view(), name='album_create'),
    path('album/<int:pk>/delete/', AlbumDeleteView.as_view(), name='album_delete'),
    path('album/<int:pk>/update/', AlbumUpdateView.as_view(), name='album_update'),
    path('photo/<int:pk>/genuuid/', PhotoTokenGenerate.as_view(), name='generate_token'),
    path('photo/<uuid:photo_id>/', PhotoTokenDetailView.as_view(), name='photo_token'),
]