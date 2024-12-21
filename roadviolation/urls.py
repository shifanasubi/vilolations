"""
URL configuration for roadviolation project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from complaints import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('violations/add/',views.ViolationsCreateView.as_view(),name="violations-create"),
    path('signup/',views.SignUpView.as_view(),name="signup"),
    path('signin/',views.SignInView.as_view(),name="signin"),
    path('violations/list/',views.ViolationsListView.as_view(),name="road-list"),
    path('violations/delete/<int:pk>/',views.ViolationsDeleteView.as_view(),name="road-delete"),
    path('violations/update/<int:pk>/',views.ViolationsUpdateView.as_view(),name="road-update"),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
