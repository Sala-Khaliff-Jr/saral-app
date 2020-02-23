from django.urls import path

from . import views
urlpatterns = [
    path('mobilegames',views.mobile_games_view,name='mobile_games_view'),
    path('pcgame',views.pc_game_view,name='pc_game_page'),
]   
