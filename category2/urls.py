from django.urls import path

from . import views
urlpatterns = [
    path('scribble',views.scribble_view,name='scribble_page'),
    path('brushhour',views.brush_hour_view,name='brush_hour_page'),
]   
