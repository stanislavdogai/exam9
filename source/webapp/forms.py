from django import forms

from webapp.models import Photo, Album


class PhotoForm(forms.ModelForm):
    def __init__(self,request, *args, **kwargs):
        super(PhotoForm, self).__init__(*args, **kwargs)
        self.fields['album'].queryset = Album.objects.filter(author_album=request.user)

    class Meta:
        model = Photo
        exclude = ['author', 'private', 'favorites']

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        exclude = ['author_album', 'created_at', 'private', 'favorites']