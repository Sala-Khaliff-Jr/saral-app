from django.shortcuts import render

# Create your views here.
def scribble_view(request):
    return render(request,'category2/scribble.html')

def brush_hour_view(request):
    return render(request,'category2/brushhour.html')
def henna_art_view(request):
    return render(request,'category2/hennaart.html')

def war_of_words_view(request):
    return render(request,'category2/warofwords.html')

def the_underrated_trouper_view(request):
    return render(request,'category2/theunderratedtrouper.html')

def anniyan_view(request):
    return render(request,'category2/anniyan.html')

def just_a_min_view(request):
    return render(request,'category2/justamin.html')    

def groove_glam_view(request):
    return render(request,'category2/grooveglam.html')        

def shake_it_up_view(request):
    return render(request,'category2/shakeitup.html')        

def raga_view(request):
    return render(request,'category2/raga.html') 

def listen_to_beat_view(request):
    return render(request,'category2/listentobeat.html')    