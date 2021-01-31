"""TextTraders URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from trade import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name='home'),

    # Auth
    path('signup/', views.signupuser, name='signupuser'),
    path('logout/', views.logoutuser, name='logoutuser'),
    path('login/', views.loginuser, name='loginuser'),

    # Books
    path('userhome/', views.userhome, name='userhome'),
    path('publishbook/', views.publishbook, name='publishbook'),
    path('academic/', views.academic, name='academic'),
    path('non-academic/', views.nonacademic, name='non-academic'),
    path('bookdetails/<int:book_pk>/',views.bookdetails, name='bookdetails'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
