from django.urls import path
from pretty_num import views
urlpatterns = [
    path('list/', views.list_pretty_num, name='list_pretty_num'),
    path('add/', views.add_pretty_num, name='add_pretty_num'),
    path('<int:nid>/edit/', views.edit_pretty_num, name='edit_pretty_num'),
    path('delete/', views.delete_pretty_num, name='delete_pretty_num'),
]