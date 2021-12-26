from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('search/', views.search, name='search'),
    path('search/res/', views.searchResult, name='js-search')
]