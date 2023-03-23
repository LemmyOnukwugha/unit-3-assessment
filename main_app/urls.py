from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.createWidget, name='widget_create'),
    path('delete/<int:widget_id>', views.deleteWidget, name='widget_delete'),
]

