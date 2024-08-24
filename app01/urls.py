from django.urls import path
from app01 import views

urlpatterns = [
    path('list/', views.depart_list),
    path('add/', views.depart_add),
    path('delete/', views.depart_delete),
    path('<int:nid>/edit/', views.depart_edit),

]