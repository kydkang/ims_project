from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('dept/<int:id>/', views.IndexListView.as_view(), name='index_list'),
    path('dept/<int:id1>/index/<int:pk>', views.IndexDetailView.as_view(), name='index_detail')
]