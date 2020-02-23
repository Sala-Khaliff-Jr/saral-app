from django.urls import path

from . import views
urlpatterns = [
    path('scribble',views.scribble_view,name='scribble_page'),
    path('brushhour',views.brush_hour_view,name='brush_hour_page'),
    path('justamin',views.just_a_min_view,name='just_a_min_page'),
    path('grooveglam',views.groove_glam_view,name='groove_glam_pages'),
    path('shakeitup',views.shake_it_up_view,name='shake_it_up_page'),
    path('raga',views.raga_view,name='raga_page'),
    path('listentobeat',views.listen_to_beat_view,name='listen_to_beat_page'),
]   
