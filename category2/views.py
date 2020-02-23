from django.shortcuts import render

# Create your views here.
def scribble_view(request):
    return render(request,'category2/scribble.html')

def brush_hour_view(request):
    return render(request,'category2/brushhour.html')

def just_a_min_view(request):
    return render(request,'category2/justamin.html')    

def groove_glam_view(request):
    return render(request,'category2/grooveglam.html')        

def shake_it_up_view(request):
    return render(request,'category2/shakeitup.html')        

