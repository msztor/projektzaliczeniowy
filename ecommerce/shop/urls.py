from django.urls import path


from . import views


urlpatterns = [
    path('', views.welcome_view),
    path('products', views.product_list)
]