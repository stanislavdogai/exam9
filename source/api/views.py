from http import HTTPStatus

from rest_framework.response import Response
from rest_framework.views import APIView

from webapp.models import Photo


class FavoritesPhoto(APIView):
    def get(self, request, *args, **kwargs):
        photo = Photo.objects.get(pk=kwargs['pk'])
        if request.user in photo.favorites.all():
            photo.favorites.remove(request.user)
            return Response({}, status=HTTPStatus.OK)
        else:
            photo.favorites.add(request.user)
            photo.save()
            return Response({}, status=HTTPStatus.OK)
