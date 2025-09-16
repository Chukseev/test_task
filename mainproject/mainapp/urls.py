from django.urls import path
from .views import AddItemToOrderView, OrderListView, ProductListView
from rest_framework.permissions import AllowAny
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

urlpatterns = [
    path("orders/<int:order_id>/items/", AddItemToOrderView.as_view(permission_classes=[AllowAny]), name="add_item"),
    path('orders/', OrderListView.as_view(permission_classes=[AllowAny]), name='order-list'),
    path('products/', ProductListView.as_view(permission_classes=[AllowAny]), name='product-list'),

    path('schema/', SpectacularAPIView.as_view(permission_classes=[AllowAny]), name='schema'),

    path('docs/', SpectacularSwaggerView.as_view(url_name='schema', permission_classes=[AllowAny]), name='swagger-ui'),

    path('redoc/', SpectacularRedocView.as_view(url_name='schema', permission_classes=[AllowAny]), name='redoc'),
]
