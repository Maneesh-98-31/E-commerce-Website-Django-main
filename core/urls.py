from django.urls import path
from core import views
from .views import (HomeView, ItemDetailView, add_to_cart, remove_from_the_cart, OrderSummary,
                    remove_single_from_the_cart, CheckoutView, PaymentView, AddCouponView,
                    RequestRefundView, add_likes_to_product, CustomerProfileView, add_comment_to_item,
                    SSLPayment, complete, complete_payment, seller, seller_submit)

app_name = 'core'

urlpatterns = [
     path('',
          HomeView.as_view(), name='item_list'),
     path('item_list/<category_name>/',
          HomeView.as_view(), name='item_list_by_category'),
     path('checkout/',
          CheckoutView.as_view(), name='checkout'),
     path('payment/<payment_option>/',
          PaymentView.as_view(), name="payment"),
     path('products/<slug>/',
          ItemDetailView.as_view(), name='products'),
     path('order_summary/',
          OrderSummary.as_view(), name='order_summary'),
     path('customer_profile/',
          CustomerProfileView.as_view(), name='customer_profile'),
     path('add_to_cart/<slug>/',
          add_to_cart, name='add_to_cart'),
     path('remove_from_the_cart/<slug>/',
          remove_from_the_cart, name='remove_from_the_cart'),
     path('remove_single_from_the_cart/<slug>/',
          remove_single_from_the_cart, name='remove_single_from_the_cart'),
     path('add_coupon/',
          AddCouponView.as_view(), name="add_coupon"),
     path('request_refund/',
          RequestRefundView.as_view(), name="request_refund"),
     path('add_likes_to_product/<slug>/',
          add_likes_to_product, name="likes"),
     path('add_comment_to_item/<slug>/',
          add_comment_to_item, name="comments"),
     path('seller/',views.seller, name="sellers"),
     path('ssl_payment/', SSLPayment.as_view(), name='ssl_payment'),
     path('complete/', complete, name='complete'),
     path('complete_payment/<tran_id>/<payment_type>/',
          complete_payment, name='complete_payment'),
     path('sr/',views.sr,name="sr"),
    # path('user/',views.user,name="user"),
     path('seller/seller_submit',views.seller_submit,name='seller_submit')



]
