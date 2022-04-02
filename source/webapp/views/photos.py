from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView

from webapp.forms import PhotoForm
from webapp.models import Photo, Album



class PhotoIndexView(LoginRequiredMixin, ListView):
    model = Photo
    context_object_name = 'photos'
    template_name = 'photos/index.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(private=False)
        return queryset.order_by('-created_at')


class PhotoDetailView(DetailView):
    model = Photo
    template_name = 'photos/view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        favorite = self.object.favorites.all()
        context['favorite'] = favorite
        return context

class PhotoCreateView(LoginRequiredMixin, CreateView):
    model = Photo
    form_class = PhotoForm
    template_name = 'photos/create.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def form_valid(self, form):
        photo = form.save(commit=False)
        photo.author = self.request.user
        photo.save()
        return redirect('web:photo_index')

    def get_photo_form(self):
        form_kwargs = {'instance' : self.object.profile}
        if self.request.method == 'POST':
            form_kwargs['data'] = self.request.POST
            form_kwargs['files'] = self.request.FILES
        return PhotoForm(**form_kwargs)

class PhotoDeleteView(PermissionRequiredMixin, DeleteView):
    model = Photo
    template_name = 'photos/delete.html'
    success_url = reverse_lazy('webapp:photo_index')
    permission_required = 'webapp.delete_photo'

    def has_permission(self):
        return super().has_permission() or self.request.user == self.get_object().author

class PhotoUpdateView(PermissionRequiredMixin, UpdateView):
    model = Photo
    form_class = PhotoForm
    template_name = 'photos/update.html'
    permission_required = 'webapp.change_photo'

    def get_product_form(self):
        form_kwargs = {'instance': self.object.profile}
        if self.request.method == 'POST':
            form_kwargs['data'] = self.request.POST
            form_kwargs['files'] = self.request.FILES
        return PhotoForm(**form_kwargs)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def has_permission(self):
        return super().has_permission() or self.request.user == self.get_object().author