"""
URL configuration for psychoapp project.

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
import psychoapp.views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import login_view, register_view, ver_historial, eliminar_historial

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', psychoapp.views.index, name='home'),
    path('about/', psychoapp.views.about, name='about'),
    path('chat/', psychoapp.views.chat, name='chat'),
    path('process_symptoms/', psychoapp.views.process_symptoms, name='process_symptoms'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('historial/', ver_historial, name='ver_historial'),
    path('historial/eliminar/<int:id>/', eliminar_historial, name='eliminar_historial'),
    path('edit_user/', psychoapp.views.edit_user, name='edit_user'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
