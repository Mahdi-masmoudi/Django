from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    
    #####################################################################
    
    path('listProduits', views.listProd, name='Produit'),
    path('editProduit', views.editProd, name='edit'),
    path('viewProd/<int:product_id>/view',views.product_det, name='product_det'),
    path('product_det', views.product_det, name='product_det'),
    path('updateProd/<int:product_id>/edit/', views.edit_product, name='edit_product'),
    path('delete/<int:id>/', views.deleteProd, name='deleteProd'),
    
    ###################################################################
    
    path('nouvFourbisseur/', views.addfourni, name='addfourni'),
    path('mesFournisseur', views.Mesfourniseur, name='four'),
    path('deletefounisseur/<int:id>/', views.deletefou, name='deletefourni'),
    path('viewFour/<int:id>/view',views.fourni_det, name='fourni_det'),
    path('fourni_det', views.fourni_det, name='fourni_det'),
    path('updatefour/<int:id>/edit/', views.edit_four, name='edit_four'),
   
    ###################################################################
   path('listcommande/', views.listCommande, name='com'),
   ############################################################""
    path('register/', views.register, name='register'),
   

   
]
