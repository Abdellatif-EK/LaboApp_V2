from django.urls import path
from django.contrib import admin

from . import views
from django.conf import settings
from django.conf.urls.static import static
from membre.models import Utilisateur

urlpatterns = [
    path('login', views.connexion, name = "connexion"),
    path('deconnexion', views.deconnexion, name = "deconnexion"),
    path('creation', views.user_creat, name = "creation"),
    path('administration', views.index , name = "index"),
    path('ajout/', views.add , name = "ajout"),
    path('update/<int:id>/', views.update , name = "update"),
    # path('administration', views.administrer , name = "adminn")
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)