
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('devadmin/', admin.site.urls),
    path('core/', include('core.urls')),
    path('api/v1/', include('api.urls')),

]
