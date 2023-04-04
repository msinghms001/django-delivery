from django.urls import path,include
from .import views

urlpatterns = [
    path('land/', views.test.as_view()),
    path('blog/', views.test.as_view()),
    path('book/', views.bookv.as_view()),
    path('author/', views.authorv.as_view()),
    # path('core/', include('core.urls')),
    # path('api/v1/', include('api.urls')),
]