from django.contrib import admin
from comentario.actions import aprova_comentario, reprova_comentario

from comentario.models import Comentario


class ComentarioAdmin(admin.ModelAdmin):
    list_display = ["usuario", "data", "aprovado"]
    actions = [reprova_comentario, aprova_comentario]


admin.site.register(Comentario, ComentarioAdmin)
