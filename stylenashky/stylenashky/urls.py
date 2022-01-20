"""stylenashky URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from main.views import main_view, all_video, detail_product, product_all


from main.views import main_view, phone_form_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_view, name='main_view'),
    path('phone_submit/', phone_form_view, name='phone_submit'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api-auth/all_video/', all_video),
    path('api-auth/product/<int:id>', detail_product),
    path('api-auth/product/', product_all)
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)