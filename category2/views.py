from django.shortcuts import render

# Create your views here.
def scribble_view(request):
    return render(request,'category2/scribble.html')

def brush_hour_view(request):
    return render(request,'category2/brushhour.html')