from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.http.request import HttpRequest
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor')
    exclude = ['autor',]

    def _autor(autor, instance):
        return f'{instance.autor.get_full_name()}'
    
    # função sobrescrita que limita a visualização dos posts apenas ao usuário logado
    def get_queryset(self, request):
        qs = super(PostAdmin, self).get_queryset(request)
        return qs.filter(autor=request.user)
    
    # anterior ao save, recupera o autor logado e salva automaticamente no objeto
    def save_model(self, request, obj, form, change):
        obj.autor = request.user
        super().save_model(request, obj, form, change)