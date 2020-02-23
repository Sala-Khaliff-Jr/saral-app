from django.urls import path

from . import views
urlpatterns = [
    path('index',views.index_page_view,name='index_page'),
]   
