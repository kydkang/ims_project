from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='index_home'),
    path('dept/<int:did>/', views.IndexListView.as_view(), name='index_list'),
    # path('dept/<int:did>/index/<int:pk>', views.IndexDetailView.as_view(), name='index_detail'),
    path('dept/<int:did>/index/new', views.IndexCreateView.as_view(), name='index_new'),
    path('dept/<int:did>/index/<int:pk>/update', views.IndexUpdateView.as_view(), name='index_update'),
    path('dept/<int:did>/index/<int:pk>/delete', views.IndexDeleteView.as_view(), name='index_delete'), 

    path('dept/<int:did>/index/<int:pk>', views.IndexDataListView.as_view(), name='indexdata_list'),
    path('dept/<int:did>/index/<int:pk>/indexdata/<int:datapk>', views.IndexDataDetailView.as_view(), name='indexdata_detail'), 
    path('dept/<int:did>/index/<int:pk>/indexdata/new', views.IndexDataCreateView.as_view(), name='indexdata_new'), 
    path('dept/<int:did>/index/<int:pk>/indexdata/<int:datapk>/update', views.IndexDataUpdateView.as_view(), name='indexdata_update'),
    path('dept/<int:did>/index/<int:pk>/indexdata/<int:datapk>/delete', views.IndexDataDeleteView.as_view(), name='indexdata_delete'), 
     
]
