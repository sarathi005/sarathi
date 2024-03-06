from django.urls import path 
from .import views
from django.contrib.auth import views as auth_views 
urlpatterns = [
    path('',views.home,name="home"),
    path('register',views.register,name="register"),
    path('login',views.login_page,name="login"),
    path('logout',views.logout_page,name="logout"),
    
    path('cart',views.cart_page,name="cart"),
    path('addtocart',views.add_to_cart,name="addtocart"),
    path('remove_cart/<str:cid>',views.remove_cart,name="remove_cart"),

    path('fav',views.fav_page,name="fav"),
    path('favourite',views.favourite_page,name="favourite"),
    path('remove_fav/<str:cid>',views.remove_fav,name="remove_fav"),

    path('collection',views.collection,name="collection"),
    path('collection/<str:name>',views.collectionview,name="collection"),
    path('collection/<str:cname>/<str:pname>',views.product_details,name="product_details"),

    path('contacts',views.contact,name="contacts"),
    path('about',views.about.as_view(),name="about"),

    
]
