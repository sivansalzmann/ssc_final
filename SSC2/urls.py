"""SSC2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from accounts import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homePage, name="home"),

    path('register/',views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutPage, name="logout"),

    path('form/',views.formPage, name="form"),
    path('report/',views.reprtPage, name="report"),
    path('update/<int:id>/',views.formPage, name="update"),
    path('delete/<int:id>/',views.deleteReport, name="delete"),
    path('private/',views.privatePage, name="private"),
    path('progress/<str:pk_report>',views.progressPage, name="progress"),

    path('manage_reports/',views.manage_reports, name="manage_reports"),
    path('manage_users/',views.manage_users, name="manage_users"),

]
