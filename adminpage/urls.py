from django.urls import path
from adminpage import views

urlpatterns = [
    path('list/', views.list_admin, name='list'),
    path('add/', views.add_admin, name='add'),
    path('<int:nid>/reset/', views.reset_pwd, name='reset'),
    path('delete/', views.delete_admin, name='delete'),
    path('<int:nid>/edit/', views.edit_admin, name='edit'),
]
