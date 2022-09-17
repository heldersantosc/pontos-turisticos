def reprova_comentario(modeladmin, request, queryset):
    queryset.update(aprovado=False)


def aprova_comentario(modeladmin, request, queryset):
    queryset.update(aprovado=True)


reprova_comentario.short_description = "Reprovar comentário"
aprova_comentario.short_description = "Aprovar comentário"
