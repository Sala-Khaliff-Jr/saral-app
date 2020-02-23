from django.urls import path

from . import views
urlpatterns = [
    path('',views.index_page_view,name='index'),
    path('index',views.index_page_view,name='index_page'),
    path('posterdesign', views.poster_design_view, name='poster_design_view'),
    path('memescreations', views.memes_creations_view, name='memes_creation_view'),
    path('thirdeye', views.third_eye_view, name='third_eye_view'),
    path('inkit', views.ink_it_view, name='ink_it_view'),
    path('naalaiyabharathi', views.naalaiya_bharathi_view, name='ink_it_view'),
    path('penapoem', views.pen_a_poem_view, name='pen_a_poem_view'),
    path('directorchair', views.director_chair_view, name='director_chair_view'),
]   
