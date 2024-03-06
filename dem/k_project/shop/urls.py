from django.urls import path
from . import views 
urlpatterns = [
    path('',views.home,name="home"),
    path('register',views.register,name="register"),
    path('collection',views.collection,name="collection"),
    path('collection/<str:name>',views.collectionsview,name="collection"),
    path('collections/<str:cname>/<str:pname>',views.prduct_details,name="product_details"),
]
