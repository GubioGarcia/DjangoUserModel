from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor')

    def _autor(autor, instance):
        return f'{instance.autor.get_full_name()}'