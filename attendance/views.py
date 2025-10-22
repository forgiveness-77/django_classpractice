from django.shortcuts import redirect, render
from attendance.forms import StudentForm
from attendance.models import Attendance,Student
from django.utils import timezone

# Create your views here.
def attendance_list(request):
    records= Attendance.objects.select_related('student').order_by('-date')
    return render(request, 'attendance/attendance_list.html', {
        'records':records
    })

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            form = StudentForm()
            return render(request, 'attendance/add_student.html', {'form': form, 'message':'User saved successfully!'})
    else:
        form = StudentForm()
    return render(request, 'attendance/add_student.html', {'form': form})

def mark_attendance(request):
    students = Student.objects.all()
    date= timezone.now().date()
    if request.method == 'POST':

        print(request.POST)


        for student in students:
            is_present = f'student_{student.id}' in request.POST
            Attendance.objects.update_or_create(
                student=student,
                date=date,
                defaults = {'present': is_present}
            )

        return redirect('/attendance/attendance_list')
    return render(request, 'attendance/mark_attendance.html', {'students':students})