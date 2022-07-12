from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user_images/', views.user_images),
    path('modify_image/<int:id>', views.modify_image),
    path('upload_image/', views.upload_image),
]