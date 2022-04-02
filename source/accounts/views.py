from django.contrib.auth import login, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.views.generic import DetailView

from accounts.forms import MyUserCreateForm

User = get_user_model()

def register_view(request):
    form = MyUserCreateForm()
    if request.method == 'POST':
        form = MyUserCreateForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            url = request.GET.get('next')
            if url:
                return redirect(url)
            return redirect('webapp:home_page')
    return render(request, 'registration/registration.html', {'form' : form})

class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = get_user_model()
    template_name = 'profile.html'
    context_object_name = 'user_obj'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        photos = self.object.photo.all()
        favorites = self.object.favorite_photo.filter(private=False)
        albums = self.object.album.all()
        context['photos'] = photos
        context['albums'] = albums
        context['favorites'] = favorites
        return context
