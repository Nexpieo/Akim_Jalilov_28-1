"""
URL configuration for online_store project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf.urls.static import static

from products.views import hello_view, now_date_view, goodby_view, products_view, main_page, product_detail_view, create_product_view
from online_store import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello_view),
    path('now_date/', now_date_view),
    path('goodby/', goodby_view),

    path('', main_page),
    path('products/', products_view),

    path('products/create/', create_product_view),
    path('products/<int:id>/', product_detail_view)
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

