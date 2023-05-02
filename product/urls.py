from django.urls import path

from . import views

urlpatterns = [
    path('category/', views.CategoryViewSet.as_view(
        {'get': 'list', 'post': 'create'}
    )),
    path('product/', views.ProductViewSet.as_view(
        {'get': 'list', 'post': 'create'}
    )),
    path('order/', views.OrderViewSet.as_view(
        {'get': 'list', 'post': 'create'}
    ))
]