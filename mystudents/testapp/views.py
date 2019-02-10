from django.shortcuts import render
from testapp.models import Student
# Create your views here.
def student_view(request):
    #students=Student.objects.all()
    students=Student.objects.all().order_by('marks')
    #students=Student.objects.all().order_by('-marks')
    #students=Student.objects.filter(marks__gt=35)
    #students=Student.objects.filter(name__startswith='N')
    return render(request, 'testapp/index.html', {'students': students})