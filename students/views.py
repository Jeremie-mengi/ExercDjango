from django.shortcuts import render
from .models import Student

def liste_students(request):

    students =  Student.objects.all()
    
    return render(request, 'student/list.html', {'student' :students})
