from django.shortcuts import render, redirect
from .models import Credit,Electrical,Civil,Mechanical,Quantity,Mechanic,Metallugy,Industrial,Chemical,Textile

import math
import json


from django.http import FileResponse
import os
from django.conf import settings

from django.contrib.auth import forms


coase=[]
year=0
coarses=[]
link='mama'
g='mama'
grades = []
semister=0


def home(request):
    return render(request,'home.html')

def year(request):
    global year
    if request.method == 'POST':
        selected_year = request.POST.get('year')
        if selected_year=='first':
            year=1
            return redirect('coarses')
        elif selected_year=='second':
            year=2
            return redirect('coarses')
        elif selected_year=='third':
            year=3
            return redirect('coarses')
        elif selected_year=='fourth':
            year=4
            return redirect('coarses')
        else:
            return redirect('home')
    return render(request,'year.html')

def coarses1(request):
    if request.method == 'POST':
        selected_coarse = request.POST.get('coarse')
        if selected_coarse=='electrical':
            return redirect('electrical')
        elif selected_coarse=='civil':
            return redirect('civil')
        elif selected_coarse=='mechanical':
            return redirect('mechanical')
        elif selected_coarse=='quantity':
            return redirect('quantity')
        elif selected_coarse=='textile':
            return redirect('textile')
        elif selected_coarse=='mining':
            return redirect('mining')
        elif selected_coarse=='geomatics':
            return redirect('geomatics')
        elif selected_coarse=='metallugy':
            return redirect('metallugy')
        elif selected_coarse=='industrial':
            return redirect('industrial')
        elif selected_coarse=='chemical':
            return redirect('chemical')
        else:
            return redirect('home')
        
    return render(request,'coarses.html')


 
def coment(request):
    return render(request,'coment.html')

def help(request):
    if request.method == 'POST':
        selected_degree = request.POST.get('help')
        selected_degree
        return redirect('about')
    return render(request, 'help.html')


def serve_image(request, image_name):
    file_path = os.path.join(settings.TEMPLATES[0]['DIRS'][0], 'images', image_name)
    return FileResponse(open(file_path, 'rb'), content_type='image/png')




#chemical views
def chemical(request):
    global semister
    if request.method == 'POST':
        selected_sem = request.POST.get('semister')
        if selected_sem=='semister2':
            semister=2
            return redirect('chemical_sem')
        elif selected_sem=='semister1':
            semister=1
            return redirect('chemical_sem')
    return render(request,'chemical.html')

def chemical_sem(request):
    global coase,grades,year,link
    coase = []
    grades=[] 
    link='industrial_sem' # Reset grades list
    if year==1:
        if semister==2:
            for i in range(8):
                j=i+1
                item=Chemical.objects.get(id=j)
                cozi=item.coarse
                coase.append(cozi)
                print(cozi)
        elif semister==1:
            for i in range(9,17):
                j=i+1
                item=Chemical.objects.get(id=j)
                cozi=item.coarse
                coase.append(cozi)
                print(cozi)

        #not yet
    elif year==2:
        if semister==2:
           for i in range(7):
                j=i+1
                item=Electrical.objects.get(id=f'{j}')
                cozi=item.coarse
                coase.append(cozi)
        elif semister==1:
            for i in range(8,16):
                j=i+1
                item=Electrical.objects.get(id=f'{j}')
                cozi=item.coarse
                coase.append(cozi)
    


    print(year)
    if request.method == 'POST':
        course_count = request.POST.get('course_count')
        courses = []
        grades=[]
        if semister==2:
            sem=8
        elif semister==1:
            sem=8

        for i in range(sem):
            j=i+1
            marks = request.POST.get(f'course{j}')
            # courses.append(marks)
            if marks in ["A", "a"]: grades.append(5)
            elif marks in ["B+", "b+"]: grades.append(4)
            elif marks in ["B", "b"]: grades.append(3)
            elif marks in ["C", "c"]: grades.append(2)
            elif marks in ["D", "d", "E", "e"]: grades.append(0)
        print(grades)
        # print(grades)
        if semister==2:
            gpa =(12 * (grades[0] + grades[1] + grades[2]) + 
                8 * (grades[3]+ grades[4] + grades[5]+grades[6]) +4*grades[7])/ 72
        elif semister==1:
            gpa =(12 * (grades[0] + grades[1] + grades[2]+grades[3]) + 
                8 * (grades[4] + grades[5] + grades[6]) + 
                4 * grades[7]) / 76
        

        gpa = math.floor(gpa * 10) / 10.0
        item=Credit.objects.create(credit=f'{gpa}')
        if gpa >=4.4:
            item1=Credit.objects.get(credit='first_class')
            coment=item1.desc
        elif gpa <4.4 and gpa >=3.5:
            item1=Credit.objects.get(credit='upper_second')
            coment=item1.desc
        elif gpa <3.5 and gpa >=2.7:
            item1=Credit.objects.get(credit='lower_second')
            coment=item1.desc
        elif gpa<=2.6 and gpa>=2.0:
            item1=Credit.objects.get(credit='pass')
            coment=item1.desc
        print(gpa)
        context = {'grade': gpa,'coment':coment,'link':link}
        return render(request, 'results.html', context)
    return render(request,'chemical_inputs.html',{'coase':coase})
######################################################################################################33333333333333




#Textile views
def textile(request):
    global semister
    if request.method == 'POST':
        selected_sem = request.POST.get('semister')
        if selected_sem=='semister2':
            semister=2
            return redirect('textile_sem')
        elif selected_sem=='semister1':
            semister=1
            return redirect('textile_sem')
    return render(request,'textile.html')

def textile_sem(request):
    global coase,grades,year,link
    coase = []
    grades=[] 
    link='industrial_sem' # Reset grades list
    if year==1:
        if semister==2:
            for i in range(6):
                j=i+1
                item=Textile.objects.get(id=j)
                cozi=item.coarse
                coase.append(cozi)
                print(cozi)
        elif semister==1:
            for i in range(7,14):
                j=i+1
                item=Textile.objects.get(id=j)
                cozi=item.coarse
                coase.append(cozi)
                print(cozi)

        #not yet
    elif year==2:
        if semister==2:
           for i in range(7):
                j=i+1
                item=Electrical.objects.get(id=f'{j}')
                cozi=item.coarse
                coase.append(cozi)
        elif semister==1:
            for i in range(8,16):
                j=i+1
                item=Electrical.objects.get(id=f'{j}')
                cozi=item.coarse
                coase.append(cozi)
    


    print(year)
    if request.method == 'POST':
        course_count = request.POST.get('course_count')
        courses = []
        grades=[]
        if semister==2:
            sem=8
        elif semister==1:
            sem=8

        for i in range(sem):
            j=i+1
            marks = request.POST.get(f'course{j}')
            # courses.append(marks)
            if marks in ["A", "a"]: grades.append(5)
            elif marks in ["B+", "b+"]: grades.append(4)
            elif marks in ["B", "b"]: grades.append(3)
            elif marks in ["C", "c"]: grades.append(2)
            elif marks in ["D", "d", "E", "e"]: grades.append(0)
        print(grades)
        # print(grades)
        if semister==2:
            gpa =(12 * (grades[0] + grades[1] + grades[2]) + 
                8 * (grades[3]+ grades[4] + grades[5]) )/ 60
        elif semister==1:
            gpa =(12 * (grades[0] + grades[1] + grades[2]+grades[3]) + 
                8 * (grades[4] + grades[5] + grades[6]) + 
                4 * grades[7]) / 76
        

        gpa = math.floor(gpa * 10) / 10.0
        item=Credit.objects.create(credit=f'{gpa}')
        if gpa >=4.4:
            item1=Credit.objects.get(credit='first_class')
            coment=item1.desc
        elif gpa <4.4 and gpa >=3.5:
            item1=Credit.objects.get(credit='upper_second')
            coment=item1.desc
        elif gpa <3.5 and gpa >=2.7:
            item1=Credit.objects.get(credit='lower_second')
            coment=item1.desc
        elif gpa<=2.6 and gpa>=2.0:
            item1=Credit.objects.get(credit='pass')
            coment=item1.desc
        print(gpa)
        context = {'grade': gpa,'coment':coment,'link':link}
        return render(request, 'results.html', context)
    return render(request,'textile_inputs.html',{'coase':coase})
######################################################################################################33333333333333




#industrial views
def industrial(request):
    global semister
    if request.method == 'POST':
        selected_sem = request.POST.get('semister')
        if selected_sem=='semister2':
            semister=2
            return redirect('industrial_sem')
        elif selected_sem=='semister1':
            semister=1
            return redirect('industrial_sem')
    return render(request,'industrial.html')

def industrial_sem(request):
    global coase,grades,year,link
    coase = []
    grades=[] 
    link='industrial_sem' # Reset grades list
    if year==1:
        if semister==2:
            for i in range(8):
                j=i+1
                item=Industrial.objects.get(id=j)
                cozi=item.coarse
                coase.append(cozi)
                print(cozi)
        elif semister==1:
            for i in range(9,17):
                j=i+1
                item=Industrial.objects.get(id=j)
                cozi=item.coarse
                coase.append(cozi)
                print(cozi)

        #not yet
    elif year==2:
        if semister==2:
           for i in range(7):
                j=i+1
                item=Electrical.objects.get(id=f'{j}')
                cozi=item.coarse
                coase.append(cozi)
        elif semister==1:
            for i in range(8,16):
                j=i+1
                item=Electrical.objects.get(id=f'{j}')
                cozi=item.coarse
                coase.append(cozi)
    


    print(year)
    if request.method == 'POST':
        course_count = request.POST.get('course_count')
        courses = []
        grades=[]
        if semister==2:
            sem=8
        elif semister==1:
            sem=8

        for i in range(sem):
            j=i+1
            marks = request.POST.get(f'course{j}')
            # courses.append(marks)
            if marks in ["A", "a"]: grades.append(5)
            elif marks in ["B+", "b+"]: grades.append(4)
            elif marks in ["B", "b"]: grades.append(3)
            elif marks in ["C", "c"]: grades.append(2)
            elif marks in ["D", "d", "E", "e"]: grades.append(0)
        print(grades)
        # print(grades)
        if semister==2:
            gpa =(12 * (grades[0] + grades[1] + grades[2]) + 
                8 * (grades[3]+ grades[4] + grades[5]+grades[6])+4*(grades[7])) / 72
        elif semister==1:
            gpa =(12 * (grades[0] + grades[1] + grades[2]+grades[3]) + 
                8 * (grades[4] + grades[5] + grades[6]) + 
                4 * grades[7]) / 76
        

        gpa = math.floor(gpa * 10) / 10.0
        item=Credit.objects.create(credit=f'{gpa}')
        if gpa >=4.4:
            item1=Credit.objects.get(credit='first_class')
            coment=item1.desc
        elif gpa <4.4 and gpa >=3.5:
            item1=Credit.objects.get(credit='upper_second')
            coment=item1.desc
        elif gpa <3.5 and gpa >=2.7:
            item1=Credit.objects.get(credit='lower_second')
            coment=item1.desc
        elif gpa<=2.6 and gpa>=2.0:
            item1=Credit.objects.get(credit='pass')
            coment=item1.desc
        print(gpa)
        context = {'grade': gpa,'coment':coment,'link':link}
        return render(request, 'results.html', context)
    return render(request,'industrial_inputs.html',{'coase':coase})
######################################################################################################33333333333333




#quantity views
def quantity(request):
    global semister
    if request.method == 'POST':
        selected_sem = request.POST.get('semister')
        if selected_sem=='semister2':
            semister=2
            return redirect('quantity_sem')
        elif selected_sem=='semister1':
            semister=1
            return redirect('quantity_sem')
    return render(request,'quantity.html')

def quantity_sem(request):
    global coase,grades,year,link
    coase = []
    grades=[] 
    link='quantity_sem' # Reset grades list
    if year==1:
        if semister==2:
            for i in range(8):
                j=i+1
                item=Quantity.objects.get(id=j)
                cozi=item.coarse
                coase.append(cozi)
                print(cozi)
        elif semister==1:
            for i in range(9,17):
                j=i+1
                item=Quantity.objects.get(id=j)
                cozi=item.coarse
                coase.append(cozi)
                print(cozi)

        #not yet
    elif year==2:
        if semister==2:
           for i in range(7):
                j=i+1
                item=Electrical.objects.get(id=f'{j}')
                cozi=item.coarse
                coase.append(cozi)
        elif semister==1:
            for i in range(8,16):
                j=i+1
                item=Electrical.objects.get(id=f'{j}')
                cozi=item.coarse
                coase.append(cozi)
    


    print(year)
    if request.method == 'POST':
        course_count = request.POST.get('course_count')
        courses = []
        grades=[]
        if semister==2:
            sem=8
        elif semister==1:
            sem=8

        for i in range(sem):
            j=i+1
            marks = request.POST.get(f'course{j}')
            # courses.append(marks)
            if marks in ["A", "a"]: grades.append(5)
            elif marks in ["B+", "b+"]: grades.append(4)
            elif marks in ["B", "b"]: grades.append(3)
            elif marks in ["C", "c"]: grades.append(2)
            elif marks in ["D", "d", "E", "e"]: grades.append(0)
        print(grades)
        # print(grades)
        if semister==2:
            gpa =(12 * (grades[0] + grades[1] + grades[2]) + 
                8 * (grades[3]+ grades[4] + grades[5]+grades[6]+grades[7])) / 76
        elif semister==1:
            gpa =(12 * (grades[0] + grades[1] + grades[2]) + 
                8 * (grades[3]+ grades[4] + grades[5]+grades[6]+grades[7])) / 76
        

        gpa = math.floor(gpa * 10) / 10.0
        item=Credit.objects.create(credit=f'{gpa}')
        if gpa >=4.4:
            item1=Credit.objects.get(credit='first_class')
            coment=item1.desc
        elif gpa <4.4 and gpa >=3.5:
            item1=Credit.objects.get(credit='upper_second')
            coment=item1.desc
        elif gpa <3.5 and gpa >=2.7:
            item1=Credit.objects.get(credit='lower_second')
            coment=item1.desc
        elif gpa<=2.6 and gpa>=2.0:
            item1=Credit.objects.get(credit='pass')
            coment=item1.desc
        print(gpa)
        context = {'grade': gpa,'coment':coment,'link':link}
        return render(request, 'results.html', context)
    return render(request,'survey_inputs.html',{'coase':coase})
######################################################################################################33333333333333





#metallugy views
def metallugy(request):
    global semister
    if request.method == 'POST':
        selected_sem = request.POST.get('semister')
        if selected_sem=='semister2':
            semister=2
            return redirect('met_sem')
        elif selected_sem=='semister1':
            semister=1
            return redirect('met_sem')
    return render(request,'metallugy.html')

def met_sem(request):
    global coase,grades,year,link
    coase = []
    grades=[] 
    link='met_sem' # Reset grades list
    if year==1:
        if semister==2:
            for i in range(8):
                j=i+1
                item=Metallugy.objects.get(id=j)
                cozi=item.coarse
                coase.append(cozi)
                print(cozi)
        elif semister==1:
            for i in range(9,17):
                j=i+1
                item=Metallugy.objects.get(id=j)
                cozi=item.coarse
                coase.append(cozi)
                print(cozi)
        print(coase)

        #not yet
    elif year==2:
        if semister==2:
           for i in range(7):
                j=i+1
                item=Electrical.objects.get(id=f'{j}')
                cozi=item.coarse
                coase.append(cozi)
        elif semister==1:
            for i in range(8,16):
                j=i+1
                item=Electrical.objects.get(id=f'{j}')
                cozi=item.coarse
                coase.append(cozi)
    


    print(year)
    if request.method == 'POST':
        course_count = request.POST.get('course_count')
        courses = []
        grades=[]
        if semister==2:
            sem=8
        elif semister==1:
            sem=8

        for i in range(sem):
            j=i+1
            marks = request.POST.get(f'course{j}')
            # courses.append(marks)
            if marks in ["A", "a"]: grades.append(5)
            elif marks in ["B+", "b+"]: grades.append(4)
            elif marks in ["B", "b"]: grades.append(3)
            elif marks in ["C", "c"]: grades.append(2)
            elif marks in ["D", "d", "E", "e"]: grades.append(0)
        print(grades)
        # print(grades)
        if semister==2:
            gpa =(12 * (grades[0] + grades[1] + grades[2]) + 
                8 * (grades[3]+ grades[4] + grades[5]+grades[6])+4*(grades[7])) / 72
        elif semister==1:
            gpa =(12 * (grades[0] + grades[1] + grades[2]+grades[3]) + 
                8 * (grades[4] + grades[5] + grades[6]) + 
                4 * grades[7]) / 76

        gpa = math.floor(gpa * 10) / 10.0
        item=Credit.objects.create(credit=f'{gpa}')
        if gpa >=4.4:
            item1=Credit.objects.get(credit='first_class')
            coment=item1.desc
        elif gpa <4.4 and gpa >=3.5:
            item1=Credit.objects.get(credit='upper_second')
            coment=item1.desc
        elif gpa <3.5 and gpa >=2.7:
            item1=Credit.objects.get(credit='lower_second')
            coment=item1.desc
        elif gpa<=2.6 and gpa>=2.0:
            item1=Credit.objects.get(credit='pass')
            coment=item1.desc
        print(gpa)
        context = {'grade': gpa,'coment':coment,'link':link}
        return render(request, 'results.html', context)
    return render(request,'met_inputs.html',{'coase':coase})
######################################################################################################33333333333333





#mechanical views
def mechanical(request):
    global semister
    if request.method == 'POST':
        selected_sem = request.POST.get('semister')
        if selected_sem=='semister2':
            semister=2
            return redirect('mech_sem')
        elif selected_sem=='semister1':
            semister=1
            return redirect('mech_sem')
    return render(request,'mechanics.html')

def mech_sem(request):
    global coase,grades,year,link
    coase = []
    grades=[] 
    link='mech_sem' # Reset grades list
    if year==1:
        if semister==2:
            for i in range(7):
                j=i+1
                item=Mechanical.objects.get(id=j)
                cozi=item.coarse
                coase.append(cozi)
                print(cozi)
        elif semister==1:
            for i in range(8):
                j=i+1
                item=Mechanic.objects.get(id=j)
                cozi=item.coarse
                coase.append(cozi)
                print(cozi)
        print(coase)
    elif year==2:
        if semister==2:
           for i in range(7):
                j=i+1
                item=Electrical.objects.get(id=f'{j}')
                cozi=item.coarse
                coase.append(cozi)
        elif semister==1:
            for i in range(8,16):
                j=i+1
                item=Electrical.objects.get(id=f'{j}')
                cozi=item.coarse
                coase.append(cozi)
    


    print(year)
    if request.method == 'POST':
        course_count = request.POST.get('course_count')
        courses = []
        grades=[]
        if semister==2:
            sem=8
        elif semister==1:
            sem=8

        for i in range(sem):
            j=i+1
            marks = request.POST.get(f'course{j}')
            # courses.append(marks)
            if marks in ["A", "a"]: grades.append(5)
            elif marks in ["B+", "b+"]: grades.append(4)
            elif marks in ["B", "b"]: grades.append(3)
            elif marks in ["C", "c"]: grades.append(2)
            elif marks in ["D", "d", "E", "e"]: grades.append(0)
            print('mama')
        print(grades)
        # print(grades)
        if semister==2:
            gpa =(12 * (grades[0] + grades[1] + grades[2]) + 
                8 * (grades[3]+ grades[4] + grades[5])+6*(grades[6])) / 66
        elif semister==1:
            gpa =(12 * (grades[0] + grades[1] + grades[2]+grades[3]) + 
                8 * (grades[4] + grades[5] + grades[6]) + 
                6 * grades[7]) / 78

        gpa = math.floor(gpa * 10) / 10.0
        item=Credit.objects.create(credit=f'{gpa}')
        if gpa >=4.4:
            item1=Credit.objects.get(credit='first_class')
            coment=item1.desc
        elif gpa <4.4 and gpa >=3.5:
            item1=Credit.objects.get(credit='upper_second')
            coment=item1.desc
        elif gpa <3.5 and gpa >=2.7:
            item1=Credit.objects.get(credit='lower_second')
            coment=item1.desc
        elif gpa<=2.6 and gpa>=2.0:
            item1=Credit.objects.get(credit='pass')
            coment=item1.desc
        print(gpa)
        context = {'grade': gpa,'coment':coment,'link':link}
        return render(request, 'results.html', context)
    return render(request,'mech_inputs.html',{'coase':coase})
######################################################################################################33333333333333




#civil views
def civil(request):
    global semister
    if request.method == 'POST':
        selected_sem = request.POST.get('semister')
        if selected_sem=='semister2':
            semister=2
            return redirect('civil_sem')
        elif selected_sem=='semister1':
            semister=1
            return redirect('civil_sem')
    return render(request,'civil.html')

def civil_sem(request):
    global coase,grades,year,link
    coase = []
    grades=[] 
    link='civil_sem' # Reset grades list
    if year==1:
        if semister==2:
            for i in range(8):
                j=i+1
                item=Civil.objects.get(id=f'{j}')
                cozi=item.coarse
                coase.append(cozi)
                print(cozi)
        elif semister==1:
            for i in range(9,17):
                j=i+1
                item=Civil.objects.get(id=f'{j}')
                cozi=item.coarse
                coase.append(cozi)
                print(cozi)
        print(coase)
    elif year==2:
        if semister==2:
           for i in range(7):
                j=i+1
                item=Electrical.objects.get(id=f'{j}')
                cozi=item.coarse
                coase.append(cozi)
        elif semister==1:
            for i in range(8,16):
                j=i+1
                item=Electrical.objects.get(id=f'{j}')
                cozi=item.coarse
                coase.append(cozi)
    


    print(year)
    if request.method == 'POST':
        course_count = request.POST.get('course_count')
        courses = []
        grades=[]
        if semister==2:
            sem=8
        elif semister==1:
            sem=8

        for i in range(sem):
            j=i+1
            marks = request.POST.get(f'course{j}')
            # courses.append(marks)
            if marks in ["A", "a"]: grades.append(5)
            elif marks in ["B+", "b+"]: grades.append(4)
            elif marks in ["B", "b"]: grades.append(3)
            elif marks in ["C", "c"]: grades.append(2)
            elif marks in ["D", "d", "E", "e"]: grades.append(0)
            print('mama')
        print(grades)
        # print(grades)
        if semister==2:
            gpa =(12 * (grades[0] + grades[1] + grades[2]) + 
                10 * (grades[3]) +8*( grades[4] + grades[5]+grades[6]) + 
                4 * grades[7]) / 74
        elif semister==1:
            gpa =(12 * (grades[0] + grades[1] + grades[2]+grades[3]) + 
                8 * (grades[4] + grades[5] + grades[6]) + 
                4 * grades[7]) / 76

        gpa = math.floor(gpa * 10) / 10.0
        item=Credit.objects.create(credit=f'{gpa}')
        if gpa >=4.4:
            item1=Credit.objects.get(credit='first_class')
            coment=item1.desc
        elif gpa <4.4 and gpa >=3.5:
            item1=Credit.objects.get(credit='upper_second')
            coment=item1.desc
        elif gpa <3.5 and gpa >=2.7:
            item1=Credit.objects.get(credit='lower_second')
            coment=item1.desc
        elif gpa<=2.6 and gpa>=2.0:
            item1=Credit.objects.get(credit='pass')
            coment=item1.desc
        print(gpa)
        context = {'grade': gpa,'coment':coment,'link':link}
        return render(request, 'results.html', context)
    return render(request,'civil_inputs.html',{'coase':coase})
######################################################################################################33333333333333

##       electrical
def first_year_electrical(request):
    global semister
    if request.method == 'POST':
        selected_sem = request.POST.get('semister')
        if selected_sem=='semister2':
            semister=2
            return redirect('elec_sem')
        elif selected_sem=='semister1':
            semister=1
            return redirect('elec_sem')
    return render(request,'electrical1.html')


def elec_sem(request):

    global coase,grades,year
    coase = []
    grades=[]
    link='elec_sem' 
    print(year) # Reset grades list
    if year==1:
        if semister==2:
            for i in range(7):
                j=i+1
                item=Electrical.objects.get(id=f'{j}')
                coz=item.coarse
                coase.append(coz)
        elif semister==1:
            for i in range(8,16):
                j=i+1
                item=Electrical.objects.get(id=f'{j}')
                coz=item.coarse
                coase.append(coz)

    elif year==2:
        if semister==1:
           for i in range(18,25):
                j=i+1
                item=Electrical.objects.get(id=f'{j}')
                coz=item.coarse
                coase.append(coz)
        elif semister==2:
            for i in range(27,34):
                j=i+1
                item=Electrical.objects.get(id=f'{j}')
                coz=item.coarse
                coase.append(coz)
        elif year==3:
            coase.append('SORRY,SERVICE IS NOT AVAILABLE FOR THIS YEAR OF STUDY')
        elif year==4:
            coase.append('SORRY,SERVICE IS NOT AVAILABLE FOR THIS YEAR OF STUDY')
            
    if request.method == 'POST':
        course_count = request.POST.get('course_count')
        courses = []
        grades=[]
        if semister==2:
            sem=7
        elif semister==1:
            sem=8

        for i in range(sem):
            j=i+1
            marks = request.POST.get(f'course{j}')
            # courses.append(marks)
            if marks in ["A", "a"]: grades.append(5)
            elif marks in ["B+", "b+"]: grades.append(4)
            elif marks in ["B", "b"]: grades.append(3)
            elif marks in ["C", "c"]: grades.append(2)
            elif marks in ["D", "d", "E", "e"]: grades.append(0)
            
        print(grades)
        # print(grades)
        if semister==2:
            gpa =(12 * (grades[0] + grades[1] + grades[2]) + 
                8 * (grades[3] + grades[4] + grades[5]) + 
                4 * grades[6]) / 64
        elif semister==1:
            gpa =(12 * (grades[0] + grades[1] + grades[2]+grades[3]) + 
                8 * (grades[4] + grades[5] + grades[6]) + 
                4 * grades[7]) / 76

        gpa = math.floor(gpa * 10) / 10.0
        item=Credit.objects.create(credit=f'{gpa}')
        if gpa >=4.4:
            item1=Credit.objects.get(credit='first_class')
            coment=item1.desc
        elif gpa <4.4 and gpa >=3.5:
            item1=Credit.objects.get(credit='upper_second')
            coment=item1.desc
        elif gpa <3.5 and gpa >=2.7:
            item1=Credit.objects.get(credit='lower_second')
            coment=item1.desc
        elif gpa<=2.6 and gpa>=2.0:
            item1=Credit.objects.get(credit='pass')
            coment=item1.desc
        print(gpa)
        context = {'grade': gpa,'coment':coment,'link':link}
        return render(request, 'results.html', context)
    return render(request,'electrical_inputs.html',{'coase':coase})
#############################################################################################################
