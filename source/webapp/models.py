from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

class Photo(models.Model):
    photography = models.ImageField(upload_to='images/', null=False, blank=False, verbose_name='Фотография')
    signature = models.CharField(max_length=200, null=False, blank=False, verbose_name='Подпись')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    author = models.ForeignKey(User, related_name='photo', on_delete=models.CASCADE, blank=False, verbose_name='Автор')
    album = models.ForeignKey('webapp.Album', blank=True, on_delete=models.CASCADE, related_name='photo', verbose_name='Альбом')
    private = models.BooleanField(default=True, verbose_name='Приват')
    favorites = models.ManyToManyField(User, null=True, blank=True, related_name='favorite_photo')
    token = models.UUIDField(editable=False, null=True, blank=True)

    class Meta:
        db_table = 'Photos'
        verbose_name = 'Photo'
        verbose_name_plural = 'Photos'



class Album(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False, verbose_name='Название')
    description = models.TextField(max_length=2000, null=True, blank=True, verbose_name='Описание')
    author_album = models.ForeignKey(User, related_name='album', on_delete=models.CASCADE, blank=False, verbose_name='Автор')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    private = models.BooleanField(default=True, verbose_name='Приват')
    favorites = models.ManyToManyField(User, null=True, blank=True, related_name='favorite_album')

    class Meta:
        db_table = 'Albums'
        verbose_name = 'Album'
        verbose_name_plural = 'Album'

    def __str__(self):
        return f"{self.name}"