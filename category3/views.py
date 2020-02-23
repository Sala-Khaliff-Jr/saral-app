from django.shortcuts import render

# Create your views here.
def mobile_games_view(request):
    return render(request,'category3/mobilegames.html')

def pc_game_view(request):
    return render(request,'category3/pcgame.html')