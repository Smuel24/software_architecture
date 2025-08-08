from django.urls import path
from .views import HomePageView
from .views import AboutPageView
from .views import ProductIndexView
from .views import ProductShowView
from .views import ProductCreateView
from .views import ProductCreateView

urlpatterns = [
     path('', HomePageView.as_view(), name='home'),
     path('about/', AboutPageView.as_view(), name='about'),
     path('products/', ProductIndexView.as_view(), name ='index'),
     path('products/<str:id>', ProductShowView.as_view(), name='show'),
     path('products/create', ProductCreateView.as_view(), name = 'form'),
     path('products/created/', ProductIndexView.as_view(), name='product-created'), 
]
