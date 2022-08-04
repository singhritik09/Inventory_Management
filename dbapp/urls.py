from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name="index"),
    path('add',views.add,name="add"),
    path('inventory',views.inventory,name="inventory"),
    path('product/<int:pk>',views.product,name='product')
    
]
