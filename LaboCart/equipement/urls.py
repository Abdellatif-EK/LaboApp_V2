from django.urls import path
from . import views
from membre import views as vs
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('public-test', views.public_test, name='public_test'),
    path('home', views.home, name = "home"),
    path('recherche', views.recherhce, name = "recherche"),
    path('search/', views.search_equipments, name='search-equipments'),
    #path('Matrice', views.matrice_page, name = "matrice_page"),
    path('Matrice_selected', views.matrice_pagel, name = "matrice_pagel"),
    path('matrice-detail/<int:app_id>/', views.matrice_detail, name='matrice_detail'),
    path('upload_excel/<int:equipement_id>/', views.upload_excel, name='upload_excel'),
    path('download_excel/<int:equipement_id>/', views.download_excel, name='download_excel'),
    path('labo1', views.voirChimio, name = "labo1"),
    path('labo2', views.voirPhysico, name = "labo2"),
    path('equip2', views.vEquipp, name = "equip2"),
    path('equipement-detail/appareil/<int:app_id>/update', views.Equip_update, name = "equip-update"),
    path('equipement-detail/appareil_Img/<int:app_id>/update', views.Equip_Img_update, name = "Equip_Img_update"),
    path('equipement-detail/appareil_pdf/<int:app_id>/update', views.Equip_pdf_update, name = "Equip_pdf_update"),
    path('deconnexion', vs.deconnexion, name = "deconnexion"),
    path('login', vs.connexion, name = "connexion"),
    path('equip1', views.vEquipc, name = "equip1"),  
    path('equipement-detail2/<str:name>/', views.equipement_detail2, name = "equipement-detail2"), 
    path('equipement-detail1/<str:name>/', views.equipement_detail1, name = "equipement-detail1"), 
    path('equipement-detail/appareil/<int:app_id>/', views.appareil_detail, name = "appareil-detail"),
    path('equipement-detail/appareil/<int:app_id>/img_delete', views.Update_img, name = "Update_img"),
    path('equipement-detail/appareil/<int:image_id>/img_update', views.replace_image, name = "replace_image"),
    path('add_matrice_line/<int:equipement_id>/', views.add_matrice_line, name='add_matrice_line'),
    path('edit/<int:matrice_line_id>/', views.edit, name='edit'),
    path('edit_retour/<int:matrice_line_id>/', views.edit_retour, name='edit_retour'),
    path('delete/<int:matrice_line_id>/', views.delete, name='delete'),
    path('delete_all_matrice/<int:equipement_id>/', views.delete_all_matrice, name='delete_all_matrice'),
    path('exporter_liste/', views.exporter_liste, name='exporter_liste'),
    path('generate_excel/', views.generate_excel, name='generate_excel'),
    path('contact/', views.contact, name='contact'),
    path('all/', views.all_equipments, name='all_equipments'),
    path('generate_pdf/', views.generate_pdf, name='generate_pdf'),
    path('add-equipement/', views.add_equipement, name='add-equipement'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)