from http import HTTPStatus

from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.response import Response
from rest_framework.views import APIView

from webapp.models import Photo, Album


class FavoritesPhoto(LoginRequiredMixin, APIView):
    def get(self, request, *args, **kwargs):
        photo = Photo.objects.get(pk=kwargs['pk'])
        if request.user in photo.favorites.all():
            photo.favorites.remove(request.user)
            return Response({}, status=HTTPStatus.OK)
        else:
            photo.favorites.add(request.user)
            photo.save()
            return Response({}, status=HTTPStatus.OK)


class FavoritesAlbum(LoginRequiredMixin, APIView):
    def get(self, request, *args, **kwargs):
        album = Album.objects.get(pk=kwargs['pk'])
        if request.user in album.favorites.all():
            album.favorites.remove(request.user)
            return Response({}, status=HTTPStatus.OK)
        else:
            album.favorites.add(request.user)
            album.save()
            return Response({}, status=HTTPStatus.OK)
