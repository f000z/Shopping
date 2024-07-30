from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('blog/', blog, name='blog'),
    path('blog-detail/', blog_detail, name='blog-detail'),
    path('contact/', contact, name='contact'),
    path('home-02/', home_02, name='home-02'),
    path('home-03/', home_03, name='home-03'),
    path('product/', product, name='product'),
    path('product-detail/', product_detail, name='product-detail'),
    path('shoping-cart/', shoping_cart, name='shoping-cart')
]
