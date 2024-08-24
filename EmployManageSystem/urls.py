"""EmployManageSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from login.views import logout
from login.views import captcha

urlpatterns = [
    # path('depart/list/', views.depart_list),
    # path('depart/add/', views.depart_add),
    # path('depart/delete/', views.depart_delete),
    # path('depart/<int:nid>/edit/', views.depart_edit),
    path('depart/', include('app01.urls')),
    path('user/', include('user.urls')),
    path('admin/', include('adminpage.urls')),
    path('pretty_num/', include('pretty_num.urls')),
    path('login/', include('login.urls')),
    path('logout/', logout, name='logout'),
    path('image/code/', captcha, name='captcha'),
]
