from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('dept/<int:did>/', views.IndexListView.as_view(), name='index_list'),
    path('dept/<int:did>/index/<int:pk>', views.IndexDetailView.as_view(), name='index_detail'),
    path('dept/<int:did>/new', views.IndexDetailView.as_view(), name='index_new'),
]
