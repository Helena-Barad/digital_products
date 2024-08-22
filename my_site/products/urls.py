from django.urls import path, include
from .views import (productdetailAPIVIEW, productlistAPIVIEW, 
                    filelistapiview, filedetailapiview
)
urlpatterns = [
    path('product/', productlistAPIVIEW.as_view(), name='product-list'),
    path('product/<int:pk>/', productdetailAPIVIEW.as_view(), name='product-detail'),
    path('product/file/', filelistapiview.as_view()),
    path('product/file/<int:pk>/', filedetailapiview.as_view()),
]