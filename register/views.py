from django.shortcuts import render
from .models import Registrations
import random
# Create your views here.
def register_view(request):
    if(request.method == "GET"):
        if 'email' in request.session:
            student_name = request.session['student_name']
            return(render(request,'register.html',{'submit':'ALREADY','student_name':student_name }))
        else:
            return(render(request,'register.html',{'submit':'NO'}))
    if(request.method=="POST"):
        # print(request.POST.get('name'))
        # print(request.POST.get('college'))
        # try:
        student_name = request.POST.get('name')
        email_id = request.POST.get('email')
        college_name = request.POST.get('college')

        Registrations.objects.create(student_name=student_name,email_id=email_id,college_name=college_name,reg_id=random.randint(20000,20000))
        register = Registrations.objects.get(email_id=email_id)
        # print(Registrations.objects.filter(email_id=email_id))
        Registrations.objects.filter(email_id=email_id).update(reg_id="SARAL00"+str(register.id))   
        register = Registrations.objects.get(email_id=email_id)
        request.session['student_name'] = student_name
        request.session['email'] = email_id
        return(render(request,'register.html',{'submit':'Yes','student_name':student_name,'id':register.reg_id}))
        # except:
        #     return(render(request,'register.html',{'submit':'NO'}))
def view_registrations(request):
    registrations = Registrations.objects.all()
    return render(request,'viewreg.html',{'registrations':registrations})