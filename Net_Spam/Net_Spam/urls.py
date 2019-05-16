"""Net_Spam URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.views.generic import TemplateView,RedirectView
from django.conf.urls.static import static

from Net_Spam import settings
from app_spam import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',views.loginPage,name='login'),

    path('admin1/',views.showAdmin,name='admin1'),
    path('a_validate/',views.admin_validation,name='a_validate'),
    path('upload_product/',views.upload_Product,name='upload_product'),
    path('upload_validate/',views.upload_Validate,name="upload_validate"),
    path('viewall/',views.viewallProducts,name="viewall"),
    path('user/',views.userPage,name='user'),
    path('u_validate/',views.u_validate,name='u_validate'),
    path('u_viewall/',views.showAllProducts,name='u_viewall'),
    path('store_orders<int:pk>/',views.storeOrders,name='store_orders'),
    path('myorders/',views.myOrders,name='myorders'),
    path('post_comment<int:pk>/',views.postComment,name='post_comment'),
    path('comment_save/',views.saveComment,name='comment_save'),
    path('userlogout/',views.uLogout,name='userlogout'),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
