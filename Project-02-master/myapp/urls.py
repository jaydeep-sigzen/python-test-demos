from django.urls import path
from .import views

urlpatterns = [
   
    path('',views.index,name='index'),
    path('shop-details/',views.shop_details,name='shop-details'),
    path('contact/',views.contact,name='contact'),
    path('shop/',views.shop,name='shop'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('change-password/',views.change_password,name='change-password'),
    path('edit-profile/',views.edit_profile,name='edit-profile'),
    path('seller-index/',views.seller_index,name='seller-index'),
    path('add-product/',views.add_product,name='add-product'),
    path('my-product/',views.my_product,name='my-product'),
    path('seller-product-details/<int:pk>/',views.seller_product_details,name='seller-product-details'),
    path('edit-product/<int:pk>/',views.edit_product,name='edit-product'),
    path('delete-product/<int:pk>/',views.delete_product,name='delete-product'),
    path('details/<int:pk>/',views.details,name='details'),
    path('add-to-wishlist/<int:pk>/',views.add_to_wishlist,name='add-to-wishlist'),
    path('add-to-cart/<int:pk>/',views.add_to_cart,name='add-to-cart'),
    path('remove-to-cart<int:pk>/',views.remove_to_cart,name='remove-to-cart'),
    path('remove-to-wishlist/<int:pk>/',views.remove_to_wishlist,name='remove-to-wishlist'),
    path('wishlist/',views.wishlist,name='wishlist'),
    path('cart/',views.cart,name='cart'),
    path('pay/',views.initiate_payment, name='pay'),
    path('callback/',views.callback, name='callback'),
    path('contact-me/',views.contact_me,name='contact-me'),
    path('confirm-oder/',views.confirm_oder,name='confirm-oder'),
   


]