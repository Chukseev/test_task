from django.urls import path
from .views import AddItemToOrderView, OrderListView, ProductListView

urlpatterns = [
    path("orders/<int:order_id>/items/", AddItemToOrderView.as_view(), name="add_item"),
    path('orders/', OrderListView.as_view(), name='order-list'),
    path('products/', ProductListView.as_view(), name='product-list'),
]
