"""catalogue URL Configuration

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
from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from menu import views


urlpatterns = [
    path('', views.index, name='index'),  # Starting page
    path('admin/', admin.site.urls),  # Admin panel
    path('api/menulist/', views.MenuAPIView.as_view()),  # GET all items
    path('api/menulist/add', views.MenuAddItemAPIView.as_view(), name='menuitem-add'),  #PUT add a new item
    path('api/menulist/<int:id>', views.RetrieveItemAPIView.as_view(), name='menuitem-detail'),  #GET display item by id
    path('api/menulist/del/<int:id>', views.DeleteItemAPIView.as_view(), name='menuitem-delete'),  #DElETE item by id
    path('api/menulist/update/<int:id>', views.MenuItemUpdateAPIView.as_view(), name='menuitem-update'),  #PUT update item by id
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

"""
Semi-working login and quarter-working logout. Usage is not recommended!
# path('login/', views.LoginView.as_view(), name='login'),
# path('logout/', views.LogoutView.as_view(), name='logout'),
"""


