
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home.as_view(), name='homeView'),
    path('accounts/', include('accounts.urls')),
    path('post/', include('posts.urls'))
]
