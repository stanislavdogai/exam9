from django.shortcuts import get_object_or_404, redirect
from django.views import View
from django.views.generic import CreateView, DetailView, UpdateView

from webapp.forms import PhotoForm, AlbumForm
from webapp.models import Album


class AlbumDetailView(DetailView):
    model = Album
    template_name = 'albums/view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        favorite = self.object.favorites.all()
        context['favorite'] = favorite
        photos = self.object.photo.all()
        context['photos'] = photos
        return context
#
class AlbumCreateView(CreateView):
    model = Album
    form_class = AlbumForm
    template_name = 'albums/create.html'

    def form_valid(self, form):
        album = form.save(commit=False)
        album.author_album = self.request.user
        album.save()
        return redirect('web:photo_index')


class AlbumDeleteView(View):
    def get(self, request, *args, **kwargs):
        album = get_object_or_404(Album, pk=kwargs.get('pk'))
        album.delete()
        return redirect('webapp:photo_index')

class AlbumUpdateView(UpdateView):
    model = Album
    form_class = AlbumForm
    template_name = 'albums/update.html'
    # permission_required = 'webapp.change_product'

    def get_product_form(self):
        form_kwargs = {'instance': self.object.profile}
        if self.request.method == 'POST':
            form_kwargs['data'] = self.request.POST
            form_kwargs['files'] = self.request.FILES
        return PhotoForm(**form_kwargs)