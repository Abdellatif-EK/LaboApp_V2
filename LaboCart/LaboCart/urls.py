from django.contrib import admin
from django.urls import path, include
from membre import  views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('equipement/', include('equipement.urls')),
    path('membre/', include('membre.urls')),
    path('membre/', include('django.contrib.auth.urls')),
    path('', views.connexion, name = "connexion")
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header= "Page d'administration"
admin.site.index_title = "Bienvenue à la page d'adminstration!"