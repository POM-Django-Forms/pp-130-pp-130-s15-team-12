from django.urls import path
from . import views

urlpatterns = [
    path('all/', views.all_orders_view, name='all_orders'), 
    path('my/', views.my_orders_view, name='my_orders'),  
    path('create/', views.create_order_view, name='create_order'), 
    path('close/<int:order_id>/', views.close_order_view, name='close_order'), 
    path('<int:order_id>/edit/', views.update_order_view, name='update_order'),

]