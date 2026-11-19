from django.shortcuts import render
from django.shortcuts import redirect
from .models import Student,Marks

# Create your views here.


def add_student(request):

    error = None

    if request.method == 'POST':
        roll = request.POST['roll']
        name = request.POST['name']
        age = request.POST['age']
        course = request.POST['course']
        Student.objects.create(

            roll = roll,
            name = name,
            age = age,
            course = course,

        )

    return render(request,'add_student.html')



def add_marks(request):
    if request.method == 'POST':
        roll = request.POST['roll']
        student = Student.objects.get(roll = roll)
        telugu = request.POST['telugu']
        english = request.POST['english']
        maths = request.POST['maths']
        science = request.POST['science']

        Marks.objects.create(

            student = student,
            telugu = telugu,
            english = english,
            maths = maths,
            science = science,

        )
    return render(request,'add_marks.html')


def view_students(request):
    student = None
    marks = None
    error = None
    if request.method == 'POST':
        roll = request.POST['roll']
        try:
            student = Student.objects.get(roll = roll)
            marks = Marks.objects.filter(student = student).first()
        except Student.DoesNotExist:
            error = "Student not found!"
    return render(request,'view_student.html',{'student':student,'marks':marks,'error':error})

def edit_student(request, id):

    student = Student.objects.get(id=id)
    error = None

    if request.method == 'POST':

        roll = request.POST['roll']

        if Student.objects.filter(roll=roll).exclude(id=id).exists():

            error = "Roll Number already exists!"

        else:

            student.roll = roll
            student.name = request.POST['name']
            student.age = request.POST['age']
            student.course = request.POST['course']

            student.save()

            return redirect('view_students')

    return render(request, 'edit_student.html', {
        'student': student,
        'error': error
    })



def update_marks(request, id):

    marks = Marks.objects.get(id=id)

    if request.method == 'POST':

        marks.telugu = request.POST['telugu']
        marks.english = request.POST['english']
        marks.maths = request.POST['maths']
        marks.science = request.POST['science']

        marks.save()

        return redirect('view_students')

    return render(request, 'update_marks.html', {'marks': marks})