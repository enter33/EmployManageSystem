from django.urls import path
from user import views

urlpatterns = [
    path('list/', views.user_list),
    path('add/', views.user_add),
    path('delete/', views.user_delete),
    path('<int:nid>/edit/', views.user_edit),
    path('model/form/add/', views.user_modelform_add),

]