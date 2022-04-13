from django.urls import path
from . import views
from .views import index
urlpatterns = [
    path('', views.ApiOverview, name='home'),
    path('add/', views.add, name='add'),
    path('view',views.view,name='view'),
    path('update/<int:pk>/', views.update, name='update'),
    path('delete/<int:pk>/', views.delete, name='delete'),
    path('demo/',index),
    path('memo/',index)
]