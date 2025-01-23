from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('signin/', views.signin),
    path('signup/', views.signup),
    path('handle_login/', views.handle_login, name='handle_login'),
    path('handle_signup/', views.handle_signup, name='handle_signup'),
    path('add-restaurant/', views.add_restaurant, name='add_restaurant'),
    path('restaurant-page/', views.restaurant_page, name='restaurant_page'),
    path('handle_login/restaurant_page/', views.restaurant_page, name='restaurant_page/'),
    path('handle_login/add_restaurant/', views.add_restaurant, name='add_restaurant/'),
    path('handle_login/show_restaurant_page/', views.show_restaurant_page, name='show_restaurant_page/'),
     
     # Restaurant-related paths
    path('restaurants/', views.show_restaurant_page, name='show_restaurant_page'),
    path('restaurants/add/', views.add_restaurant, name='add_restaurant'),
    path('restaurants/<int:restaurant_id>/', views.restaurant_page, name='restaurant_page'),
    path('restaurants/<int:restaurant_id>/menu/', views.restaurant_menu, name='restaurant_menu'),
    path('restaurants/<int:restaurant_id>/update/', views.update_restaurant, name='update_restaurant'),
    path('restaurants/<int:restaurant_id>/update/page/', views.update_restaurant_page, name='update_restaurant_page'),
    path('restaurants/<int:restaurant_id>/delete/', views.delete_restaurant, name='delete_restaurant'),

    path('menu/<int:menuItem_id>/update/', views.update_menuItem, name='update_menuItem'),
    path('menu/<int:menuItem_id>/update/page/', views.update_menuItem_page, name='update_menuItem_page'),
    path('menu/<int:menuItem_id>/delete/', views.delete_menuItem, name='delete_menuItem'),
    
    path('restaurants/<int:restaurant_id>/menu/customer/', views.customer_menu, name='customer_menu'),

    ]


   
    
