from django.urls import path,include
from .import views
urlpatterns = [

    path('', views.home,name='home'),
    path('edit/', views.edit,name='edit'),
    path('test/', views.testops),
    # path('api/v1/', include('api.urls')),

]