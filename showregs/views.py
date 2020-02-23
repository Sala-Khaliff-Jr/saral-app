from django.shortcuts import render

# Create your views here.
def show_reg_view(request):
    return render(request,'showregs.html')