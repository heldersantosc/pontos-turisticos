from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken import views

from django.conf.urls.static import static
from django.conf import settings

from core.api.viewsets import PontoTuristicoViewSet
from atracoes.api.viewsets import AtracaoViewSet
from enderecos.api.viewsets import EnderecoViewSet
from avaliacoes.api.viewsets import AvaliacaoViewSet
from comentario.api.viewsets import ComentarioViewSet

router = routers.DefaultRouter()
router.register(r"pontosturisticos", PontoTuristicoViewSet, basename="pontoturistico")
router.register(r"atracoes", AtracaoViewSet)
router.register(r"enderecos", EnderecoViewSet)
router.register(r"comentarios", ComentarioViewSet)
router.register(r"avaliacoes", AvaliacaoViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("admin/", admin.site.urls),
    path("auth/", views.obtain_auth_token),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
