# from django.shortcuts import render,redirect
# from .models import Credit






# electrical_courses=["MT171", "EE131", "DS113", "EE172", "EE152", "EE153", "EE102"]
# electrical_credits=[12, 8, 8, 12, 8, 4, 4]
# gpa=1000
# # Create your views here.
# def home(request):
   


#     return render(request,'home.html')


# electrical_credits=[{},]



# def about(request):
#     if request.method=='POST':
#         credit=request.GET.get('credit')
#         gpa=Credit.objects.GET(credit=credit) 

#         return redirect('results')
    
    
    
#     # grades = []
#     # for i in range(len(courses['courses'])):
#     #     grade = request.form.get(f'grade{i + 1}')
#     #     try:
#     #         grades.append(float(grade))
#     #     except ValueError:
#     #         grades.append(0)
#     return render(request,'about.html')

# def results(request):


#     context={'gpa':gpa}
#     return render(request,'results.html',context)