from django.urls import path
from . import views


app_name = 'tokens'

urlpatterns = [
    path('create/', views.TokenCreateView.as_view(), name='create-token'),
    path('list/', views.TokenListView.as_view(), name='get-token-list'),
    path('total_supply/', views.TotalSupplyView.as_view(), name='get-total-supply'),
]