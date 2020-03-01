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
            return(render(request,'register.html',{'submit':'NO','EVENTSELECT':'NO'}))
    if(request.method=="POST"):
        # print(request.POST.get('name'))
        # print(request.POST.get('college'))
        # try:
        email_id = request.POST.get('email')
        
        # try :
            
        print('Email Present',Registrations.objects.filter(email_id=email_id))

        if not Registrations.objects.filter(email_id=email_id):
            print("Not Existing")
        else:
            print("Existing")
            return render(request,'register.html',{'submit':'EXISTINGID'})

        student_name = request.POST.get('name')
        college_name = request.POST.get('college')
        
        print(college_name)


        events = ""
        total_cost = 0
        if request.POST.get('POSTER DESIGN') == 'on':
            events += "Poster Design, "
            total_cost += 100
        if request.POST.get('MEME CREATION') == 'on':
            events += "Meme Creation, "
            total_cost += 100 
        if request.POST.get('THIRD EYE') == 'on':
            events += "Third Eye, "
            total_cost += 100
        if request.POST.get('INK IT') == 'on':
            events += "Ink It, "
            total_cost += 100
        if request.POST.get('NAALAIYA BHARATHI') == 'on':
            events += "Naalaiya Bharathi, "
            total_cost += 100
        if request.POST.get('PEN A POEM') == 'on':
            events += "Pen A Poem, "
            total_cost += 100
        if request.POST.get('DIRECTOR CHAIR') == 'on':
            events += "Director's Chair, "
            total_cost += 300
        if request.POST.get('JUST A MINUTE') == 'on':
            events += "Just A Minute, "
            total_cost += 100
        if request.POST.get('SCRIBBLES') == 'on':
            events += "Scribbles, "
            total_cost += 100
        if request.POST.get('BRUSH HOUR') == 'on':
            events += "Brush Hour, "
            total_cost += 100
        if request.POST.get('HENNA ART') == 'on':
            events += "Henna Art, "
            total_cost += 150
        if request.POST.get('WAR OF WORDS') == 'on':
            events += "War of Words, "
            total_cost += 100
        if request.POST.get('GROOVE & GLAM') == 'on':
            events += "Groove and Glam, "
            gndgteam_size = int(request.POST.get('gndgteamsize'))
            total_cost += gndgteamsize * 50
        if request.POST.get('SHAKE IT UP') == 'on':
            events += "Shake It Up, "
            total_cost += 100
        if request.POST.get('RAGA') == 'on':
            events += "Raga, "
            total_cost += 100
        if request.POST.get('LISTEN TO MY BEAT') == 'on':
            events += "Listen To My Beat, "
            total_cost += 100
        if request.POST.get('ANNIYAN') == 'on':
            events += "Anniyan, "
            total_cost += 100
        if request.POST.get('THE UNDERRATED TROUPER') == 'on':
            events += "The Underrated Trouper, "
            total_cost += 100

        if request.POST.get('PUBG') == 'on':
            events += "Pubg, "
            if request.POST.get('mobsolo') == 'on':
                total_cost += 50
            if request.POST.get('mobsquad'):
                total_cost += 200
        if request.POST.get('Free Fire') == 'on':
            events += "Free Fire, "
            if request.POST.get('mobsolo') == 'on':
                total_cost += 50
            if request.POST.get('mobsquad'):
                total_cost += 200

        if request.POST.get('NFS MW') == 'on':
            events += "NFS Most Wanted, "
            total_cost += 100

        if request.POST.get('COD') == 'on':
            events += "COD, "
            if request.POST.get('mobsolo') == 'on':
                total_cost += 100
            if request.POST.get('mobsolo') == 'pcsquad':
                total_cost += 500 
        if (len(events) < 3 and total_cost < 50):
            return render(request,'register.html',{'submit':'NO','EVENTSELECT':'No'})
        
        print(events)

        Registrations.objects.create(student_name=student_name,email_id=email_id,college_name=college_name,reg_id=random.randint(20000,20000),events=events,total_cost=total_cost)
        register = Registrations.objects.get(email_id=email_id)
        # print(Registrations.objects.filter(email_id=email_id))
        Registrations.objects.filter(email_id=email_id).update(reg_id="SARAL00"+str(register.id))   
        register = Registrations.objects.get(email_id=email_id)
        request.session['student_name'] = student_name
        request.session['email'] = email_id
        return(render(request,'register.html',{'submit':'Yes','student_name':student_name,'id':register.reg_id,'total_cost':total_cost}))
        # except:
        #     return(render(request,'register.html',{'submit':'NO'}))
        # except:
        #     return(render(request,'register.html',{'submit':'NO'}))

def view_registrations(request):
    registrations = Registrations.objects.all()
    return render(request,'viewreg.html',{'registrations':registrations})