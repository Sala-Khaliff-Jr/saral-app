from django.shortcuts import render
from .models import Registrations
# Create your views here.
def register_view(request):
    if 'email' in request.session:
        student_name = request.session['student_name']
        return(render(request,'register.html',{'submit':'ALREADY','student_name':student_name }))
    if(request.method == "GET"):
        return(render(request,'register.html',{'submit':'NO'}))
    if(request.method=="POST"):
        # print(request.POST.get('name'))
        # print(request.POST.get('college'))
        try:
            student_name = request.POST.get('name')
            email_id = request.POST.get('email')
            request.session['student_name'] = student_name
            request.session['email'] = email_id
            Registrations.objects.create(student_name=student_name,email_id=email_id)
            reg_id = Registrations.objects.get(email_id=email_id)
            return(render(request,'register.html',{'submit':'Yes','student_name':student_name,'id':reg_id.id}))
        except:
            return(render(request,'register.html',{'submit':'NO'}))
def view_registrations(request):
    try:
        registrations = Registrations.objects.all()
        return render(request(request,'viewreg.html',{'registrations':registrations}))
    except:

