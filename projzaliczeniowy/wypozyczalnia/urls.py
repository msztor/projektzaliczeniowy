from django.urls import path


from . import views


urlpatterns = [
    path('', views.welcome_view),
    path('produkty', views.product_list, name='product-list'),
    path('produkt/<int:id>/', views.product_detail, name='product-detail')
]