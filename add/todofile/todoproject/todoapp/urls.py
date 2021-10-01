
from django.urls import path
from . import views

urlpatterns = [

    path('', views.tests, name='tasks'),
    path('delete/<int:tid>/', views.deleted, name='delete'),
    path('update/<int:taskid>/', views.updation, name='update')
]