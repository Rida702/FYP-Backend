from django.contrib import admin
from django.urls import path,include
from Ima.views import index_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', index_view, name='index'),
    path('imageApp/', include('imageApp.urls')),
]
