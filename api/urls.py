from django.urls import path

from . import views

app_name = 'api'

urlpatterns = [
    path('menu', views.MenuItemView.as_view(), name='menu'),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view(), name='menu-detail'),
]