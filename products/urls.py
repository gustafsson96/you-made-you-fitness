from django.urls import path
from . import views

urlpatterns = [
    path('', views.products_guides, name='products_guides'),
    path('<guide_id>/', views.product_guide_detail, name='product_guide_detail'),
]
