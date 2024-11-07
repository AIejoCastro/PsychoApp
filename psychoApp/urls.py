"""
URL configuration for psychoApp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
import psychoApp.views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import login_view, register_view, ver_historial, eliminar_historial

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', psychoApp.views.index, name='home'),
    path('about/', psychoApp.views.about, name='about'),
    path('chat/', psychoApp.views.chat, name='chat'),
    path('process_symptoms/', psychoApp.views.process_symptoms, name='process_symptoms'),
    path('', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('historial/', ver_historial, name='ver_historial'),
    path('historial/eliminar/<int:id>/', eliminar_historial, name='eliminar_historial'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
