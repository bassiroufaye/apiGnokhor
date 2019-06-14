from django.urls import path

from . import views

urlpatterns = [
    path('client/', views.ListClient.as_view()),
    path('client/<int:pk>/', views.DetailClient.as_view()),

    path('lunette/', views.ListLunette.as_view()),
    path('lunette/<int:pk>/', views.DetailLunette.as_view()),

    path('commande/', views.ListCommande.as_view()),
    path('commande/<int:pk>/', views.DetailCommande.as_view()),
    ]