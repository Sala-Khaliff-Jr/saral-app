from django.shortcuts import render

# Create your views here.
def index_page_view(request):
    return(render(request,'index.html'))

def poster_design_view(request):
    return(render(request,'category1/posterdesign.html'))

def memes_creations_view(request):
    return(render(request,'category1/memescreations.html'))    

def third_eye_view(request):
    return(render(request,'category1/thirdeye.html'))        

def ink_it_view(request):
    return(render(request,'category1/inkit.html'))        

def naalaiya_bharathi_view(request):
    return(render(request,'category1/naalaiyabharathi.html'))   

def pen_a_poem_view(request):
    return(render(request,'category1/penapoem.html'))

def director_chair_view(request):
    return(render(request,"category1/directorchair.html"))